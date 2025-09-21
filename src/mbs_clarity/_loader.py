import argparse
import hashlib
import logging
import time
from collections import Counter
from datetime import datetime

from mbs_clarity.db import (
    init_schema,
    insert_constraints,
    insert_items,
    insert_meta,
    insert_relations,
    reset_db,
)
from mbs_clarity.mbs_parser import parse_csv, parse_xml, to_db_rows
from mbs_clarity.relationship_extraction import extract_constraints, extract_relations

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s"
)
logger = logging.getLogger("mbs_clarity.loader")


def _file_hash(path: str | None) -> str | None:
    if not path:
        return None
    try:
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return None


def _summarize_counts(rows: list[tuple]) -> dict[str, int]:
    """Summarize counts by type from rows."""
    counts: dict[str, int] = {}
    for r in rows:
        key = r[1] if len(r) > 1 else str(r)
        counts[key] = counts.get(key, 0) + 1
    return counts


def _analyze_extraction_patterns(items: list[dict]) -> dict[str, dict]:
    """Analyze extraction patterns and coverage."""
    logger.info("Analyzing extraction patterns...")

    total_items = len(items)
    items_with_relations = 0
    items_with_constraints = 0
    items_with_both = 0

    relation_patterns = Counter()
    constraint_patterns = Counter()
    description_lengths = []

    for item in items:
        item_num = str(item.get("item_num"))
        description = item.get("description") or ""
        derived_fee = item.get("derived_fee") or None

        # Extract relations and constraints
        relations = extract_relations(item_num, description, derived_fee)
        constraints = extract_constraints(item_num, description)

        # Track patterns
        if relations:
            items_with_relations += 1
            for rel in relations:
                relation_patterns[rel[1]] += 1

        if constraints:
            items_with_constraints += 1
            for con in constraints:
                constraint_patterns[con[1]] += 1

        if relations and constraints:
            items_with_both += 1

        # Track description lengths
        description_lengths.append(len(description))

    # Calculate statistics
    avg_desc_length = (
        sum(description_lengths) / len(description_lengths)
        if description_lengths
        else 0
    )
    max_desc_length = max(description_lengths) if description_lengths else 0
    min_desc_length = min(description_lengths) if description_lengths else 0

    return {
        "total_items": total_items,
        "items_with_relations": items_with_relations,
        "items_with_constraints": items_with_constraints,
        "items_with_both": items_with_both,
        "relation_patterns": dict(relation_patterns),
        "constraint_patterns": dict(constraint_patterns),
        "description_stats": {
            "avg_length": avg_desc_length,
            "max_length": max_desc_length,
            "min_length": min_desc_length,
        },
        "coverage": {
            "relations_coverage": (
                (items_with_relations / total_items) * 100 if total_items > 0 else 0
            ),
            "constraints_coverage": (
                (items_with_constraints / total_items) * 100 if total_items > 0 else 0
            ),
            "both_coverage": (
                (items_with_both / total_items) * 100 if total_items > 0 else 0
            ),
        },
    }


def main():
    parser = argparse.ArgumentParser(
        description="Load MBS data into SQLite and extract relationships"
    )
    parser.add_argument(
        "--xml", type=str, help="Absolute path to MBS XML dataset", default=None
    )
    parser.add_argument(
        "--csv", type=str, help="Absolute path to MBS CSV dataset", default=None
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose logging"
    )
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    if not args.xml and not args.csv:
        raise SystemExit("Provide --xml or --csv path")

    logger.info("Starting MBS data loading process")
    logger.info(f"Source: {args.xml or args.csv}")

    # Reset and initialize database
    logger.info("Resetting and initializing database schema")
    reset_db()
    init_schema()

    # Parse data
    logger.info("Parsing MBS data")
    t0 = time.time()
    items = parse_xml(args.xml) if args.xml else parse_csv(args.csv)
    parse_time = (time.time() - t0) * 1000
    logger.info(f"Parsed {len(items)} items in {parse_time:.1f} ms")

    # Insert items
    logger.info("Inserting items into database")
    t0 = time.time()
    insert_items(to_db_rows(items))
    insert_time = (time.time() - t0) * 1000
    logger.info(f"Inserted {len(items)} items in {insert_time:.1f} ms")

    # Extract relationships and constraints
    logger.info("Extracting relationships and constraints")
    t0 = time.time()
    rel_rows: list[tuple] = []
    con_rows: list[tuple] = []

    for it in items:
        item_num = str(it.get("item_num"))
        description = it.get("description") or ""
        derived_fee = it.get("derived_fee") or None
        rel_rows.extend(extract_relations(item_num, description, derived_fee))
        con_rows.extend(extract_constraints(item_num, description))

    extraction_time = (time.time() - t0) * 1000
    logger.info(
        f"Extracted {len(rel_rows)} relations and {len(con_rows)} constraints in {extraction_time:.1f} ms"
    )

    # Insert relations and constraints
    logger.info("Inserting relations and constraints into database")
    t0 = time.time()
    insert_relations(rel_rows)
    insert_constraints(con_rows)
    insert_relcon_time = (time.time() - t0) * 1000
    logger.info(f"Inserted relations and constraints in {insert_relcon_time:.1f} ms")

    # Analyze extraction patterns
    analysis = _analyze_extraction_patterns(items)

    # Log detailed metrics
    logger.info("=== EXTRACTION METRICS ===")
    logger.info(f"Total items processed: {analysis['total_items']}")
    logger.info(
        f"Items with relations: {analysis['items_with_relations']} ({analysis['coverage']['relations_coverage']:.1f}%)"
    )
    logger.info(
        f"Items with constraints: {analysis['items_with_constraints']} ({analysis['coverage']['constraints_coverage']:.1f}%)"
    )
    logger.info(
        f"Items with both: {analysis['items_with_both']} ({analysis['coverage']['both_coverage']:.1f}%)"
    )

    logger.info("Description statistics:")
    logger.info(
        f"  Average length: {analysis['description_stats']['avg_length']:.1f} characters"
    )
    logger.info(
        f"  Max length: {analysis['description_stats']['max_length']} characters"
    )
    logger.info(
        f"  Min length: {analysis['description_stats']['min_length']} characters"
    )

    # Log relation patterns
    logger.info("Relation patterns (top 10):")
    sorted_relations = sorted(
        analysis["relation_patterns"].items(), key=lambda x: -x[1]
    )
    for pattern, count in sorted_relations[:10]:
        logger.info(f"  {pattern}: {count}")

    # Log constraint patterns
    logger.info("Constraint patterns (top 10):")
    sorted_constraints = sorted(
        analysis["constraint_patterns"].items(), key=lambda x: -x[1]
    )
    for pattern, count in sorted_constraints[:10]:
        logger.info(f"  {pattern}: {count}")

    # Insert metadata
    src_path = args.xml or args.csv or ""
    logger.info("Inserting metadata")
    insert_meta(
        src_path,
        _file_hash(src_path),
        len(items),
        len(rel_rows),
        len(con_rows),
        datetime.utcnow().isoformat(),
    )

    total_time = parse_time + insert_time + extraction_time + insert_relcon_time
    logger.info("=== LOADING COMPLETE ===")
    logger.info(f"Total processing time: {total_time:.1f} ms")
    logger.info(f"Items per second: {len(items) / (total_time / 1000):.1f}")
    logger.info(f"Relations per second: {len(rel_rows) / (total_time / 1000):.1f}")
    logger.info(f"Constraints per second: {len(con_rows) / (total_time / 1000):.1f}")

    # Print summary for console output
    print("\n=== MBS DATA LOADING SUMMARY ===")
    print(
        f"Loaded {len(items)} items, {len(rel_rows)} relations, {len(con_rows)} constraints"
    )
    print(f"Processing time: {total_time:.1f} ms")
    print(f"Relations coverage: {analysis['coverage']['relations_coverage']:.1f}%")
    print(f"Constraints coverage: {analysis['coverage']['constraints_coverage']:.1f}%")
    print(f"Both coverage: {analysis['coverage']['both_coverage']:.1f}%")


if __name__ == "__main__":
    main()
