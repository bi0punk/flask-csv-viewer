# flask-csv-viewer

Flask web application that allows users to upload a CSV file and display its contents as an interactive HTML table using Pandas and DataTables.

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://python.org)
[![CI](https://github.com/tu-usuario/flask-csv-viewer/actions/workflows/ci.yml/badge.svg)](https://github.com/tu-usuario/flask-csv-viewer/actions/workflows/ci.yml)

## Tabla de Contenidos

- [Características](#características)
- [Stack](#stack)
- [Arquitectura](#arquitectura)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Tests](#tests)
- [Configuración](#configuración)
- [CI](#ci)
- [Seguridad](#seguridad)
- [Limitaciones / Roadmap](#limitaciones--roadmap)
- [Licencia](#licencia)

## Características

- Subida de archivos CSV con validación de tipo y tamaño
- Renderizado como tabla HTML interactiva con DataTables
- Escapado de celdas via `pandas.to_html(escape=True)` contra XSS
- Límite de subida configurable (16 MB por defecto)

## Stack

- Python 3.11+, Flask, Pandas, DataTables (jQuery)

## Arquitectura

```
flask-csv-viewer/
├── app.py
├── templates/
│   └── index.html
├── data/               # CSVs de ejemplo
├── tests/
├── requirements.txt
├── pyproject.toml
└── .env.example
```

## Requisitos

- Python 3.11+

## Instalación

```bash
git clone https://github.com/tu-usuario/flask-csv-viewer.git
cd flask-csv-viewer
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Uso

```bash
python app.py
```

Abrir `http://localhost:5000`, seleccionar un archivo CSV y visualizarlo como tabla interactiva con búsqueda, ordenamiento y paginación.

## Tests

```bash
pip install pytest ruff
pytest -q
ruff check .
```

## Configuración

| Variable              | Default | Descripción                     |
|-----------------------|---------|---------------------------------|
| `MAX_CONTENT_LENGTH`  | 16 MB   | Tamaño máximo de subida         |

## CI

GitHub Actions ejecuta ruff lint + pytest en cada push y PR.

## Seguridad

- Los valores de las celdas CSV son escapados por pandas `to_html(escape=True)` antes de renderizar
- Tamaño de subida limitado a 16 MB
- Validación de tipo de archivo por el parser de pandas

## Limitaciones / Roadmap

- [ ] Soporte para archivos Excel (.xlsx)
- [ ] Exportación a PDF/JSON desde la tabla
- [ ] Filtros avanzados y gráficos integrados
- [ ] Subida drag & drop

## Licencia

MIT
