"""Gestión simple de base de datos para CUFE/CFDI.
Plantilla usando sqlite3 para desarrollo local.
"""

import sqlite3
from pathlib import Path
from typing import Optional

DB_PATH = Path(__file__).parent / "database.sqlite"


def get_connection(path: Optional[Path] = None) -> sqlite3.Connection:
    if path is None:
        path = DB_PATH
    conn = sqlite3.connect(str(path))
    return conn


def create_tables(conn: sqlite3.Connection) -> None:
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS cufe (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cufe TEXT UNIQUE NOT NULL,
            source_pdf TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()


if __name__ == "__main__":
    conn = get_connection()
    create_tables(conn)
    print("Tablas creadas en", DB_PATH)
