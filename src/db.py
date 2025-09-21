import sqlite3
from collections.abc import Iterable
from contextlib import contextmanager

DB_PATH = "/Users/thomasshields/MBS_Clarity/mbs.db"


@contextmanager
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()


def init_schema() -> None:
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS items (
                item_num TEXT PRIMARY KEY,
                category TEXT,
                group_code TEXT,
                schedule_fee REAL,
                description TEXT,
                derived_fee TEXT,
                start_date TEXT,
                end_date TEXT,
                provider_type TEXT,
                emsn_description TEXT
            );
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS relations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_num TEXT NOT NULL,
                relation_type TEXT NOT NULL,
                target_item_num TEXT,
                detail TEXT,
                FOREIGN KEY (item_num) REFERENCES items(item_num)
            );
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS constraints (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_num TEXT NOT NULL,
                constraint_type TEXT NOT NULL,
                value TEXT NOT NULL,
                FOREIGN KEY (item_num) REFERENCES items(item_num)
            );
            """
        )
        conn.commit()


def reset_db() -> None:
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS constraints;")
        cur.execute("DROP TABLE IF EXISTS relations;")
        cur.execute("DROP TABLE IF EXISTS items;")
        conn.commit()
        init_schema()


def insert_items(rows: Iterable[tuple]):
    with get_conn() as conn:
        cur = conn.cursor()
        cur.executemany(
            """
            INSERT OR REPLACE INTO items (
                item_num, category, group_code, schedule_fee, description, derived_fee,
                start_date, end_date, provider_type, emsn_description
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """,
            list(rows),
        )
        conn.commit()


def insert_relations(rows: Iterable[tuple]):
    with get_conn() as conn:
        cur = conn.cursor()
        cur.executemany(
            """
            INSERT INTO relations (item_num, relation_type, target_item_num, detail)
            VALUES (?, ?, ?, ?);
            """,
            list(rows),
        )
        conn.commit()


def insert_constraints(rows: Iterable[tuple]):
    with get_conn() as conn:
        cur = conn.cursor()
        cur.executemany(
            """
            INSERT INTO constraints (item_num, constraint_type, value)
            VALUES (?, ?, ?);
            """,
            list(rows),
        )
        conn.commit()


def fetch_item_aggregate(item_num: str):
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM items WHERE item_num = ?", (item_num,))
        item_row = cur.fetchone()
        cur.execute(
            "SELECT relation_type, target_item_num, detail FROM relations WHERE item_num = ?",
            (item_num,),
        )
        rel_rows = cur.fetchall()
        cur.execute(
            "SELECT constraint_type, value FROM constraints WHERE item_num = ?",
            (item_num,),
        )
        con_rows = cur.fetchall()
        return item_row, rel_rows, con_rows


def fetch_items_like(item_nums: list[str]):
    placeholders = ",".join(["?"] * len(item_nums))
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(
            f"SELECT item_num FROM items WHERE item_num IN ({placeholders})", item_nums
        )
        return [r[0] for r in cur.fetchall()]
