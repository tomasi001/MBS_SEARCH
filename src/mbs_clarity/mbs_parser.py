from __future__ import annotations

import os
import time
from collections.abc import Iterable

import pandas as pd
from lxml import etree

# Canonical output field names
KEY_FIELDS = {
    "ItemNum": "item_num",
    "Category": "category",
    "Group": "group_code",
    "ScheduleFee": "schedule_fee",
    "Description": "description",
    "DerivedFee": "derived_fee",
    "ItemStartDate": "start_date",
    "ItemEndDate": "end_date",
    "ProviderType": "provider_type",
    "EMSNDescription": "emsn_description",
}

# Alternative XML tag name variants occasionally seen
ALT_FIELDS: dict[str, list[str]] = {
    "ItemNum": ["ItemNumber", "Item", "Number"],
    "Group": ["GroupCode"],
    "ScheduleFee": ["Fee", "Schedule_Fee"],
    "Description": ["ItemDescriptor", "ItemDescription", "ItemText"],
    "ItemStartDate": ["StartDate", "EffectiveFrom"],
    "ItemEndDate": ["EndDate", "EffectiveTo"],
    "ProviderType": ["Provider", "ProviderClass"],
}


def _text(elem) -> str | None:
    if elem is None:
        return None
    if hasattr(elem, "text"):
        return (elem.text or "").strip() or None
    return str(elem)


def _coerce_float(value: str | None) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except Exception:
        return None


def _first_by_localnames(node, names: list[str]):
    # Search child or descendant nodes matching any local-name in names
    for nm in names:
        found = node.xpath(f".//*[local-name()='{nm}'][1]")
        if found:
            return found[0]
    return None


def _find_local(node, primary: str):
    # Try primary name then alternatives
    names = [primary] + ALT_FIELDS.get(primary, [])
    return _first_by_localnames(node, names)


def parse_xml(xml_path: str) -> list[dict]:
    t0 = time.time()
    with open(xml_path, "rb") as f:
        tree = etree.parse(f)
    root = tree.getroot()

    # Find all elements that have an ItemNum-like child (namespace agnostic)
    candidates = root.xpath(
        "//*[ *[local-name()='ItemNum' or local-name()='ItemNumber' or local-name()='Item' or local-name()='Number'] ]"
    )
    items: list[dict] = []
    for node in candidates:
        item_num_el = _find_local(node, "ItemNum")
        item_num = _text(item_num_el)
        if not item_num:
            continue
        rec: dict[str, object] = {"item_num": item_num}
        for xml_key, out_key in KEY_FIELDS.items():
            if xml_key == "ItemNum":
                continue
            el = _find_local(node, xml_key)
            val = _text(el)
            if out_key == "schedule_fee":
                rec[out_key] = _coerce_float(val)
            else:
                rec[out_key] = val
        items.append(rec)

    elapsed = (time.time() - t0) * 1000
    print(f"Parsed {len(items)} items from XML in {elapsed:.1f} ms")
    return items


def parse_csv(csv_path: str) -> list[dict]:
    t0 = time.time()
    if not os.path.exists(csv_path):
        raise FileNotFoundError(csv_path)
    df = pd.read_csv(csv_path, dtype=str, keep_default_na=False, na_filter=False)

    # Normalize columns to expected names if possible
    colmap: dict[str, str] = {}
    for src, dst in KEY_FIELDS.items():
        for col in df.columns:
            if col.lower() == src.lower():
                colmap[col] = dst
                break
    if "item_num" not in colmap.values():
        # try to find item number column
        for col in df.columns:
            if col.lower() in ("itemnum", "item_num", "item number", "item"):
                colmap[col] = "item_num"
                break

    # Find source column name for item number
    itemnum_src_cols = [k for k, v in colmap.items() if v == "item_num"]
    if not itemnum_src_cols:
        print("Warning: No item number column found in CSV header")
        return []
    itemnum_src = itemnum_src_cols[0]

    out: list[dict] = []
    for _, row in df.iterrows():
        item_num_val = row.get(itemnum_src)
        item_num = (item_num_val or "").strip()
        if not item_num:
            continue
        rec: dict[str, object] = {"item_num": item_num}
        for src_col, dst_key in colmap.items():
            if dst_key == "item_num":
                continue
            val = row.get(src_col)
            if isinstance(val, str):
                val = val.strip()
            # Normalize empties
            if val in (None, ""):
                norm = None
            else:
                norm = val
            if dst_key == "schedule_fee":
                rec[dst_key] = _coerce_float(norm) if isinstance(norm, str) else None
            else:
                rec[dst_key] = norm
        out.append(rec)

    elapsed = (time.time() - t0) * 1000
    print(f"Parsed {len(out)} items from CSV in {elapsed:.1f} ms")
    return out


def to_db_rows(items: Iterable[dict]) -> list[tuple]:
    rows: list[tuple] = []
    for it in items:
        rows.append(
            (
                it.get("item_num"),
                it.get("category"),
                it.get("group_code"),
                it.get("schedule_fee"),
                it.get("description"),
                it.get("derived_fee"),
                it.get("start_date"),
                it.get("end_date"),
                it.get("provider_type"),
                it.get("emsn_description"),
            )
        )
    return rows
