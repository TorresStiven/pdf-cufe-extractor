# 📄 PDF CUFE Extractor

Aplicación en **Python** para procesar archivos PDF, extraer metadatos y detectar el **CUFE/CFDI**, guardando los resultados en una base de datos SQLite.

Una herramienta simple, modular y orientada a facilitar la extranccion ed informacion relevante en facturación.

---

## 🎯 Resumen

- Procesa todos los PDFs en la carpeta `pdfs/`.
- Extrae: nombre del archivo, número de páginas, tamaño en bytes y CUFE (si existe).
- Persiste los resultados en SQLite y muestra estadísticas por consola.

---

## 🧱 Estructura del proyecto

```text
pdf_cufe_extractor/
├── pdfs/                 # Carpeta para colocar los PDFs a procesar
├── database/             # (vacía) para archivos relacionados con la BD
├── extractor.py          # Lógica de extracción y detección de CUFE
├── database.py           # Lógica de persistencia (SQLite)
├── main.py               # Script principal (orquestador)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Tecnologías

- Python 3.8+
- pdfplumber (extracción de texto desde PDFs)
- SQLite (persistencia ligera)
- re (expresiones regulares)
- pathlib (manejo de rutas)

---

## 📦 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/TorresStiven/pdf-cufe-extractor.git
cd pdf_cufe_extractor
```

2. (Opcional) Crea y activa un entorno virtual:

- Linux / macOS

```bash
python -m venv venv
source venv/bin/activate
```

- Windows (PowerShell)

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

> Si aún no existe `requirements.txt`, instala `pdfplumber` y cualquier dependencia necesaria: `pip install pdfplumber`.

---

## ▶️ Uso

1. Coloca tus archivos PDF dentro de `pdfs/`.
2. Ejecuta el script principal:

```bash
python main.py
```

Al finalizar, los resultados se almacenan en `reports.db` (por defecto) y verás un resumen por consola.

---

## 📊 Ejemplo de salida

```
Inicializando base de datos...
Se encontraron 3 archivos PDF.

Procesando: factura_01.pdf
Procesando: factura_02.pdf
Procesando: factura_03.pdf

Proceso finalizado.
PDFs procesados: 3
PDFs con CUFE encontrado: 2
PDFs sin CUFE: 1
```

---

## 🗄 Esquema de la base de datos

Tabla: `pdf_reports`

- `id` INTEGER PRIMARY KEY AUTOINCREMENT
- `filename` TEXT
- `pages` INTEGER
- `cufe` TEXT (puede ser NULL)
- `size_bytes` INTEGER

---

## 💡 Buenas prácticas y próximas mejoras

- Añadir validaciones y pruebas unitarias.
- Usar `with sqlite3.connect(...) as conn:` para gestionar conexiones de forma segura.
- Añadir logging con `logging` en lugar de `print` para mayor control.
- Exportar reportes a CSV/JSON o incluir CLI con opciones (click/argparse).
- Mejorar la validación del CUFE si se dispone de su formato exacto.

---

## 👤 Autor

Stiven Torres — Proyecto desarrollado como ejercicio práctico.
