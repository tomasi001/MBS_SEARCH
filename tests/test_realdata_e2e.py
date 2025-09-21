import os
import tempfile
from collections import Counter

import pytest
from fastapi.testclient import TestClient
from mbs_clarity.db import (
    init_schema,
    insert_constraints,
    insert_items,
    insert_meta,
    insert_relations,
    reset_db,
    set_db_path,
)
from mbs_clarity.mbs_parser import parse_xml, to_db_rows
from mbs_clarity.relationship_extraction import extract_constraints, extract_relations

from api.main import app


def _classify_item(it: dict[str, object]) -> tuple[str, int]:
    """Classify an item by number of distinct target relations."""
    item_num = str(it.get("item_num"))
    desc = it.get("description") or ""
    rels = extract_relations(item_num, desc, it.get("derived_fee") or None)
    distinct = {(r[1]) for r in rels if r[2] is not None}
    return item_num, len(distinct)


def _count_constraint_types(it: dict[str, object]) -> Counter:
    """Count constraint types for an item."""
    item_num = str(it.get("item_num"))
    desc = it.get("description") or ""
    constraints = extract_constraints(item_num, desc)
    return Counter(c[1] for c in constraints)


@pytest.mark.skipif(
    not os.getenv("MBS_XML_PATH"), reason="Set MBS_XML_PATH to run real-data tests"
)
def test_real_data_samples_from_xml():
    """Test with real XML data - find items with different relation patterns."""
    xml_path = os.environ["MBS_XML_PATH"]
    # Parse a subset: to keep tests fast, we use the first ~800 items then classify
    items = parse_xml(xml_path)
    assert len(items) > 0

    zero: dict[str, object] | None = None
    one: dict[str, object] | None = None
    multi: dict[str, object] | None = None

    for it in items[:800]:
        item_num, n = _classify_item(it)
        if n == 0 and zero is None:
            zero = it
        elif n == 1 and one is None:
            one = it
        elif n >= 2 and multi is None:
            multi = it
        if zero and one and multi:
            break

    assert (
        zero is not None
    ), "Could not find zero-link item in sample; broaden sample size if needed"
    assert one is not None, "Could not find single-link item in sample"
    assert multi is not None, "Could not find multi-link item in sample"

    # Build a tiny DB with just these 3 items
    with tempfile.TemporaryDirectory() as td:
        db_path = os.path.join(td, "realdata.db")
        set_db_path(db_path)
        reset_db()
        init_schema()

        subset: list[dict[str, object]] = [zero, one, multi]
        insert_items(to_db_rows(subset))

        rel_rows: list[tuple] = []
        con_rows: list[tuple] = []
        for it in subset:
            item_num = str(it.get("item_num"))
            desc = it.get("description") or ""
            rel_rows.extend(
                extract_relations(item_num, desc, it.get("derived_fee") or None)
            )
            con_rows.extend(extract_constraints(item_num, desc))
        insert_relations(rel_rows)
        insert_constraints(con_rows)

        # Insert meta data
        insert_meta(
            source_path=xml_path,
            source_hash="test_hash",
            items_count=len(subset),
            relations_count=len(rel_rows),
            constraints_count=len(con_rows),
            loaded_at="2024-01-01T00:00:00",
        )

        client = TestClient(app)

        # Zero-link should have 0 relations
        r0 = client.get("/api/items", params={"codes": str(zero["item_num"])})
        assert r0.status_code == 200
        d0 = r0.json()
        assert len(d0["items"]) == 1
        assert len(d0["items"][0]["relations"]) == 0

        # One-link should have >=1 relations but only 1 distinct target
        r1 = client.get("/api/items", params={"codes": str(one["item_num"])})
        assert r1.status_code == 200
        d1 = r1.json()
        targets1 = {
            rel["target_item_num"]
            for rel in d1["items"][0]["relations"]
            if rel["target_item_num"]
        }
        assert len(targets1) == 1

        # Multi-link should have >=2 distinct targets
        rm = client.get("/api/items", params={"codes": str(multi["item_num"])})
        assert rm.status_code == 200
        dm = rm.json()
        targetsM = {
            rel["target_item_num"]
            for rel in dm["items"][0]["relations"]
            if rel["target_item_num"]
        }
        assert len(targetsM) >= 2


@pytest.mark.skipif(
    not os.getenv("MBS_XML_PATH"), reason="Set MBS_XML_PATH to run real-data tests"
)
def test_real_data_constraint_extraction():
    """Test constraint extraction with real XML data."""
    xml_path = os.environ["MBS_XML_PATH"]
    items = parse_xml(xml_path)
    assert len(items) > 0

    # Find items with different constraint patterns
    duration_items = []
    location_items = []
    provider_items = []
    requirement_items = []

    for it in items[:500]:  # Sample first 500 items
        constraint_counts = _count_constraint_types(it)

        if constraint_counts.get("duration_min_minutes", 0) > 0:
            duration_items.append(it)
        if constraint_counts.get("location", 0) > 0:
            location_items.append(it)
        if constraint_counts.get("provider", 0) > 0:
            provider_items.append(it)
        if constraint_counts.get("requirement", 0) > 0:
            requirement_items.append(it)

    # Test that we found items with each constraint type
    assert len(duration_items) > 0, "No items with duration constraints found"
    assert len(location_items) > 0, "No items with location constraints found"
    assert len(provider_items) > 0, "No items with provider constraints found"
    assert len(requirement_items) > 0, "No items with requirement constraints found"

    # Test one item from each category
    test_items = [
        duration_items[0],
        location_items[0],
        provider_items[0],
        requirement_items[0],
    ]

    with tempfile.TemporaryDirectory() as td:
        db_path = os.path.join(td, "constraints_test.db")
        set_db_path(db_path)
        reset_db()
        init_schema()

        insert_items(to_db_rows(test_items))

        rel_rows: list[tuple] = []
        con_rows: list[tuple] = []
        for it in test_items:
            item_num = str(it.get("item_num"))
            desc = it.get("description") or ""
            rel_rows.extend(
                extract_relations(item_num, desc, it.get("derived_fee") or None)
            )
            con_rows.extend(extract_constraints(item_num, desc))
        insert_relations(rel_rows)
        insert_constraints(con_rows)

        client = TestClient(app)

        # Test each item has expected constraints
        for item in test_items:
            item_num = str(item["item_num"])
            r = client.get("/api/items", params={"codes": item_num})
            assert r.status_code == 200
            data = r.json()
            assert len(data["items"]) == 1

            item_data = data["items"][0]
            constraint_types = {c["constraint_type"] for c in item_data["constraints"]}

            # Verify expected constraint types are present
            expected_constraints = _count_constraint_types(item)
            for constraint_type in expected_constraints:
                assert (
                    constraint_type in constraint_types
                ), f"Expected {constraint_type} constraint for item {item_num}"


@pytest.mark.skipif(
    not os.getenv("MBS_XML_PATH"), reason="Set MBS_XML_PATH to run real-data tests"
)
def test_real_data_relation_types():
    """Test that we can extract different relation types from real data."""
    xml_path = os.environ["MBS_XML_PATH"]
    items = parse_xml(xml_path)
    assert len(items) > 0

    # Find items with different relation types
    relation_type_counts = Counter()
    sample_items = {}

    for it in items[:1000]:  # Sample first 1000 items
        item_num = str(it.get("item_num"))
        desc = it.get("description") or ""
        rels = extract_relations(item_num, desc, it.get("derived_fee") or None)

        for rel in rels:
            rel_type = rel[1]
            relation_type_counts[rel_type] += 1
            if rel_type not in sample_items:
                sample_items[rel_type] = it

    # Verify we found multiple relation types
    assert len(relation_type_counts) > 0, "No relations found in sample"

    # Test that common relation types are present
    common_types = ["excludes", "same_day_excludes", "generic_excludes"]
    found_types = set(relation_type_counts.keys())

    for rel_type in common_types:
        if rel_type in found_types:
            # Test this relation type with a sample item
            sample_item = sample_items[rel_type]

            with tempfile.TemporaryDirectory() as td:
                db_path = os.path.join(td, f"{rel_type}_test.db")
                set_db_path(db_path)
                reset_db()
                init_schema()

                insert_items(to_db_rows([sample_item]))

                item_num = str(sample_item.get("item_num"))
                desc = sample_item.get("description") or ""
                rel_rows = extract_relations(
                    item_num, desc, sample_item.get("derived_fee") or None
                )
                con_rows = extract_constraints(item_num, desc)

                insert_relations(rel_rows)
                insert_constraints(con_rows)

                client = TestClient(app)
                r = client.get("/api/items", params={"codes": item_num})
                assert r.status_code == 200
                data = r.json()

                # Verify the relation type is present in the response
                response_rel_types = {
                    rel["relation_type"] for rel in data["items"][0]["relations"]
                }
                assert (
                    rel_type in response_rel_types
                ), f"Expected {rel_type} relation for item {item_num}"


@pytest.mark.skipif(
    not os.getenv("MBS_XML_PATH"), reason="Set MBS_XML_PATH to run real-data tests"
)
def test_real_data_api_performance():
    """Test API performance with real data samples."""
    xml_path = os.environ["MBS_XML_PATH"]
    items = parse_xml(xml_path)
    assert len(items) > 0

    # Take a larger sample for performance testing
    sample_size = min(100, len(items))
    sample_items = items[:sample_size]

    with tempfile.TemporaryDirectory() as td:
        db_path = os.path.join(td, "performance_test.db")
        set_db_path(db_path)
        reset_db()
        init_schema()

        insert_items(to_db_rows(sample_items))

        rel_rows: list[tuple] = []
        con_rows: list[tuple] = []
        for it in sample_items:
            item_num = str(it.get("item_num"))
            desc = it.get("description") or ""
            rel_rows.extend(
                extract_relations(item_num, desc, it.get("derived_fee") or None)
            )
            con_rows.extend(extract_constraints(item_num, desc))
        insert_relations(rel_rows)
        insert_constraints(con_rows)

        client = TestClient(app)

        # Test single item lookup
        import time

        start_time = time.time()
        r = client.get("/api/items", params={"codes": str(sample_items[0]["item_num"])})
        single_lookup_time = time.time() - start_time

        assert r.status_code == 200
        assert (
            single_lookup_time < 1.0
        ), f"Single lookup took {single_lookup_time:.3f}s, should be < 1s"

        # Test multiple item lookup
        codes = [str(item["item_num"]) for item in sample_items[:10]]
        start_time = time.time()
        r = client.get("/api/items", params={"codes": ",".join(codes)})
        multi_lookup_time = time.time() - start_time

        assert r.status_code == 200
        assert (
            multi_lookup_time < 2.0
        ), f"Multi lookup took {multi_lookup_time:.3f}s, should be < 2s"
        assert len(r.json()["items"]) == len(codes)
