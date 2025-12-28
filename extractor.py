import re
import pdfplumber
from pathlib import Path

carpeta = Path("pdfs")

for archivo_pdf in carpeta.glob("*.pdf"):
    print("Procesando archivo:", archivo_pdf.name)

    nombre_archivo = archivo_pdf.stem
    peso_archivo = archivo_pdf.stat().st_size

    with pdfplumber.open(archivo_pdf) as pdf:
        numero_paginas = len(pdf.pages)

        texto_completo = ""
        for pagina in pdf.pages:
            texto_pagina = pagina.extract_text()
            if texto_pagina:
                texto_completo += texto_pagina

        patron_cufe = r'(\b([0-9a-fA-F]\n*){95,100}\b)'
        resultado = re.search(patron_cufe, texto_completo)

        if resultado:
            cufe = resultado.group()
            print("CUFE encontrado")
        else:
            cufe = None
            print("CUFE no encontrado")
