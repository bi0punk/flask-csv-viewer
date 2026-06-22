# flask-csv-viewer

Flask web application that allows users to upload a CSV file and display its contents as an HTML table using Pandas and DataTables.

**Security:** Cell values are escaped by pandas `to_html(escape=True)` before rendering, preventing XSS via malicious CSV data.

## Stack

Python 3, Flask, Pandas, DataTables

## Installation

```bash
pip install flask pandas
```

## Usage

```bash
python app.py
```

Open `http://localhost:5000`, upload a CSV file, and view its contents as an interactive table.

## Security

- CSV cell content is HTML-escaped by pandas before rendering
- Upload size limited to 16 MB
- File type validation enforced by pandas parser

## License

MIT
