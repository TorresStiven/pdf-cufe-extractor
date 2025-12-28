# pdf_cufe_extractor

Script en Python para extraer el CUFE desde facturas en formato PDF
y almacenar la información en una base de datos SQLite.

## Estructura

- `pdfs/` - carpeta para colocar PDFs de ejemplo (se incluye `.gitkeep`).
- `database/` - espacio para persistencia y archivos asociados (se incluye `.gitkeep`).
- `extractor.py` - funciones para extracción y parsing de CUFE.
- `database.py` - utilidades de base de datos (SQLite por defecto).
- `main.py` - script de entrada para procesar PDFs.
