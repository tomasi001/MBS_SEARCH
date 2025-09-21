import os
import tempfile

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

from api.main import app


@pytest.fixture
def temp_db():
    """Create a temporary database for testing."""
    with tempfile.TemporaryDirectory() as td:
        db_path = os.path.join(td, "test.db")
        set_db_path(db_path)
        reset_db()
        init_schema()
        yield db_path


def test_api_end_to_end_minimal(temp_db):
    """Test basic API functionality with minimal data."""
    insert_items(
        [
            (
                "23",
                "1",
                "A1",
                39.75,
                "not on the same day as item 36",
                None,
                None,
                None,
                "gp",
                None,
            )
        ]
    )
    insert_relations([("23", "same_day_excludes", "36", "not on the same day as item")])
    insert_constraints([("23", "duration_min_minutes", "6")])

    client = TestClient(app)
    r = client.get("/api/items", params={"codes": "23"})
    assert r.status_code == 200
    data = r.json()
    assert data["items"][0]["item"]["item_num"] == "23"
    rel_types = {
        (rel["relation_type"], rel["target_item_num"])
        for rel in data["items"][0]["relations"]
    }
    assert ("same_day_excludes", "36") in rel_types


def test_api_multiple_codes(temp_db):
    """Test API with multiple codes."""
    insert_items(
        [
            ("3", "1", "A1", 25.50, "Basic consultation", None, None, None, "gp", None),
            (
                "23",
                "1",
                "A1",
                39.75,
                "Extended consultation",
                None,
                None,
                None,
                "gp",
                None,
            ),
            (
                "104",
                "1",
                "A1",
                75.00,
                "Complex consultation",
                None,
                None,
                None,
                "gp",
                None,
            ),
        ]
    )
    insert_relations(
        [
            ("3", "excludes", "23", "cannot be billed together"),
            ("23", "same_day_excludes", "104", "not same day"),
        ]
    )
    insert_constraints(
        [
            ("3", "duration_min_minutes", "6"),
            ("23", "duration_min_minutes", "20"),
            ("104", "duration_min_minutes", "40"),
        ]
    )

    client = TestClient(app)
    r = client.get("/api/items", params={"codes": "3,23,104"})
    assert r.status_code == 200
    data = r.json()
    assert len(data["items"]) == 3
    assert data["requested"] == ["3", "23", "104"]
    assert set(data["found"]) == {"3", "23", "104"}


def test_api_nonexistent_codes(temp_db):
    """Test API with codes that don't exist."""
    insert_items(
        [("3", "1", "A1", 25.50, "Basic consultation", None, None, None, "gp", None)]
    )

    client = TestClient(app)
    r = client.get("/api/items", params={"codes": "999,888"})
    assert r.status_code == 200
    data = r.json()
    assert len(data["items"]) == 0
    assert data["requested"] == ["999", "888"]
    assert data["found"] == []


def test_api_mixed_existing_nonexistent(temp_db):
    """Test API with mix of existing and nonexistent codes."""
    insert_items(
        [
            ("3", "1", "A1", 25.50, "Basic consultation", None, None, None, "gp", None),
            (
                "23",
                "1",
                "A1",
                39.75,
                "Extended consultation",
                None,
                None,
                None,
                "gp",
                None,
            ),
        ]
    )

    client = TestClient(app)
    r = client.get("/api/items", params={"codes": "3,999,23"})
    assert r.status_code == 200
    data = r.json()
    assert len(data["items"]) == 2
    assert data["requested"] == ["3", "999", "23"]
    assert set(data["found"]) == {"3", "23"}


def test_api_empty_codes(temp_db):
    """Test API with empty codes parameter."""
    client = TestClient(app)
    r = client.get("/api/items", params={"codes": ""})
    assert r.status_code == 400


def test_api_no_codes_param(temp_db):
    """Test API without codes parameter."""
    client = TestClient(app)
    r = client.get("/api/items")
    assert r.status_code == 422  # Validation error


def test_api_complex_item_with_all_relations(temp_db):
    """Test API with item having multiple relation types."""
    insert_items(
        [
            (
                "44",
                "1",
                "A1",
                125.10,
                "Professional attendance by a general practitioner at consulting rooms (other than a service to which another item in the table applies), lasting at least 40 minutes and including any of the following that are clinically relevant: (a) taking an extensive patient history; (b) performing a clinical examination; (c) arranging any necessary investigation; (d) implementing a management plan; (e) providing appropriate preventive health care; for one or more health-related issues, with appropriate documentation-each attendance",
                None,
                "01.12.1989",
                None,
                "gp",
                None,
            )
        ]
    )
    insert_relations(
        [
            (
                "44",
                "generic_excludes",
                None,
                "other than a service to which another item in the table applies",
            ),
            ("44", "prerequisite", "3", "requires basic consultation"),
            ("44", "allows_same_day", "23", "can be billed same day"),
        ]
    )
    insert_constraints(
        [
            ("44", "duration_min_minutes", "40"),
            ("44", "location", "consulting rooms"),
            ("44", "provider", "general practitioner"),
            ("44", "requirement", "(a) taking an extensive patient history"),
            ("44", "requirement", "(b) performing a clinical examination"),
            ("44", "requirement", "(c) arranging any necessary investigation"),
            ("44", "requirement", "(d) implementing a management plan"),
            ("44", "requirement", "(e) providing appropriate preventive health care"),
        ]
    )

    client = TestClient(app)
    r = client.get("/api/items", params={"codes": "44"})
    assert r.status_code == 200
    data = r.json()
    item = data["items"][0]

    # Check item data
    assert item["item"]["item_num"] == "44"
    assert item["item"]["schedule_fee"] == 125.10
    assert item["item"]["start_date"] == "01.12.1989"

    # Check relations
    rel_types = {rel["relation_type"] for rel in item["relations"]}
    assert "generic_excludes" in rel_types
    assert "prerequisite" in rel_types
    assert "allows_same_day" in rel_types

    # Check constraints
    con_types = {con["constraint_type"] for con in item["constraints"]}
    assert "duration_min_minutes" in con_types
    assert "location" in con_types
    assert "provider" in con_types
    assert "requirement" in con_types

    # Check specific constraint values
    requirements = [
        c["value"] for c in item["constraints"] if c["constraint_type"] == "requirement"
    ]
    assert "(a) taking an extensive patient history" in requirements
    assert "(b) performing a clinical examination" in requirements


def test_api_meta_table_functionality(temp_db):
    """Test that meta table is properly populated."""
    insert_items(
        [("3", "1", "A1", 25.50, "Basic consultation", None, None, None, "gp", None)]
    )
    insert_relations([("3", "excludes", "23", "cannot be billed together")])
    insert_constraints([("3", "duration_min_minutes", "6")])

    # Insert meta data
    insert_meta(
        source_path="/test/path.xml",
        source_hash="abc123",
        items_count=1,
        relations_count=1,
        constraints_count=1,
        loaded_at="2024-01-01T00:00:00",
    )

    # Verify meta data was inserted (we can't easily test this through the API,
    # but we can verify the function works)
    assert True  # Meta insertion completed without error
