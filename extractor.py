"""Extractor de CUFE/CFDI desde PDFs.
Plantilla inicial: añade funciones para extraer texto y parsear CUFE.
"""

from pathlib import Path


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extrae texto de un PDF (implementación pendiente).

    Args:
        pdf_path: Ruta al archivo PDF.

    Returns:
        Texto extraído del PDF.
    """
    # TODO: implementar extracción con PyPDF2, pdfminer.six o similar
    return ""


def parse_cufe_from_text(text: str) -> list:
    """Parsea y devuelve una lista de CUFE/CDFI encontrados en el texto."""
    # TODO: implementar patrón regex para CUFE
    return []
