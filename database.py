import sqlite3
from pathlib import Path

DB_PATH = Path("reports.db")


def get_connection():
    # sqlite3.connect acepta un Path y lo convierte a cadena internamente.
    return sqlite3.connect(DB_PATH)


def init_db():
   #Inicializa la base de datos creando la tabla `pdf_reports` si no existe.

    conn = get_connection()
    cursor = conn.cursor()

    # Sentencia SQL: crea la tabla si aún no existe
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pdf_reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT NOT NULL,
        pages INTEGER NOT NULL,
        cufe TEXT,
        size_bytes INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def insert_pdf_report(filename, pages, cufe, size_bytes):

    """
    Uso de parámetros (placeholders '?') para evitar inyección SQL y que
    sqlite3 se encargue del escape y tipo de datos.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO pdf_reports (filename, pages, cufe, size_bytes)
    VALUES (?, ?, ?, ?)
    """, (filename, pages, cufe, size_bytes))

    conn.commit()
    conn.close()


def get_all_reports():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pdf_reports")
    rows = cursor.fetchall()  # lista de tuplas: [(id, filename, pages, cufe, size), ...]

    conn.close()
    return rows


def clear_reports():
    #Borra todos los registros de `pdf_reports`.Permanentemente
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM pdf_reports")
    conn.commit()
    conn.close()
