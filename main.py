"""Entrada principal para ejecutar el extractor."""

import argparse
from pathlib import Path

from extractor import extract_text_from_pdf, parse_cufe_from_text
from database import get_connection, create_tables


def main():
    parser = argparse.ArgumentParser(description="Extrae CUFE de PDFs y los guarda en BD")
    parser.add_argument("path", help="Archivo PDF o carpeta con PDFs")
    args = parser.parse_args()

    p = Path(args.path)

    conn = get_connection()
    create_tables(conn)

    if p.is_dir():
        pdfs = list(p.glob("*.pdf"))
    else:
        pdfs = [p]

    for pdf in pdfs:
        text = extract_text_from_pdf(str(pdf))
        cufes = parse_cufe_from_text(text)
        print(f"{pdf}: {len(cufes)} CUFE(s) encontrados")


if __name__ == "__main__":
    main()
