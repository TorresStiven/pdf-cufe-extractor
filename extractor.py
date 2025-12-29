import re
import pdfplumber
from pathlib import Path

def process_pdf(archivo_pdf: Path):
    print("Procesando archivo:", archivo_pdf.name)

    nombre_archivo = archivo_pdf.stem
    peso_archivo = archivo_pdf.stat().st_size

    with pdfplumber.open(archivo_pdf) as pdf:
        numero_paginas = len(pdf.pages)

        texto_completo = ""
        for pagina in pdf.pages:
            texto_pagina = pagina.extract_text()
            if texto_pagina:
                texto_completo += texto_pagina + "\n"

        patron_cufe = r'([0-9a-fA-F]\n*){95,100}'
        resultado = re.search(patron_cufe, texto_completo)

        if resultado:
            cufe = resultado.group().replace("\n", "")
            print("CUFE encontrado")
        else:
            cufe = None
            print("CUFE no encontrado")

    return {
        "filename": nombre_archivo,
        "pages": numero_paginas,
        "cufe": cufe,
        "size_bytes": peso_archivo
    }