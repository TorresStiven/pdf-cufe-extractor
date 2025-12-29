#!/usr/bin/env python3
"""Generador de PDFs de prueba.

Crea PDFs en la carpeta `pdfs/` con información similar a facturas y, con
probabilidad ~50%, incluye un CUFE hexadecimal aleatorio de 96 caracteres.

Uso:
    python generate_pdfs.py --count 10 --output pdfs
"""

from __future__ import annotations

import argparse
import random
from datetime import date
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

CLIENTES = [
    "Cliente Alpha",
    "Cliente Beta",
    "Cliente Gamma",
    "Cliente Delta",
    "Cliente Omega",
    "Empresa Prueba SAS",
    "Comercial XYZ",
    "Servicios ABC",
]

HEX_CHARS = "0123456789abcdef"


def new_random_cufe(length: int = 96) -> str:
    """Genera un CUFE aleatorio (hexadecimal) de longitud `length`."""
    return "".join(random.choice(HEX_CHARS) for _ in range(length))


def make_pdf(path: Path, cliente: str, fecha: str, valor: int, cufe: str | None):
    """Crea un PDF simple con los campos proporcionados.

    Usa reportlab para dibujar texto en una sola página A4.
    """
    c = canvas.Canvas(str(path), pagesize=A4)
    width, height = A4

    x = 40
    y = height - 60
    line_height = 16

    lines = [
        "FACTURA ELECTRÓNICA",
        f"Cliente: {cliente}",
        f"Fecha: {fecha}",
        f"Valor total: {valor}",
    ]

    if cufe:
        lines += ["", "CUFE:", cufe]

    for line in lines:
        c.drawString(x, y, line)
        y -= line_height

    c.showPage()
    c.save()


def main(count: int, out_folder: Path):
    out_folder.mkdir(parents=True, exist_ok=True)

    for i in range(1, count + 1):
        file_name = f"venta_prueba_{i}.pdf"
        file_path = out_folder / file_name

        cliente = random.choice(CLIENTES)
        valor = random.randint(500_000, 1_500_000)
        fecha = date.today().isoformat()
        incluir_cufe = random.choice([False, True])

        cufe = new_random_cufe() if incluir_cufe else None

        make_pdf(file_path, cliente, fecha, valor, cufe)
        print("PDF creado:", file_name)

    print(f"\nProceso finalizado. PDFs generados en la carpeta '{out_folder}'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generador de PDFs de prueba")
    parser.add_argument("--count", type=int, default=10, help="Cantidad de PDFs a generar")
    parser.add_argument("--output", type=Path, default=Path("pdfs"), help="Carpeta de salida")
    args = parser.parse_args()
    main(args.count, args.output)
