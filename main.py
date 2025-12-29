from pathlib import Path

from database import init_db, insert_pdf_report
from extractor import process_pdf

PDF_FOLDER = Path("pdfs")


def main():
    print("Inicializando base de datos...")
    init_db()

    if not PDF_FOLDER.exists():
        print("La carpeta 'pdfs' no existe.")
        return

    pdf_files = list(PDF_FOLDER.glob("*.pdf"))

    if not pdf_files:
        print("No se encontraron archivos PDF para procesar.")
        return

    print(f"Se encontraron {len(pdf_files)} archivos PDF.\n")

    procesados = 0
    con_cufe = 0

    for pdf_path in pdf_files:
        print(f"Procesando: {pdf_path.name}")

        result = process_pdf(pdf_path)

        insert_pdf_report(
            filename=result["filename"],
            pages=result["pages"],
            cufe=result["cufe"],
            size_bytes=result["size_bytes"]
        )

        procesados += 1
        if result["cufe"]:
            con_cufe += 1

    print("\nProceso finalizado.")
    print(f"PDFs procesados: {procesados}")
    print(f"PDFs con CUFE encontrado: {con_cufe}")
    print(f"PDFs sin CUFE: {procesados - con_cufe}")


if __name__ == "__main__":
    main()