import os
import secrets

import pandas as pd
from flask import Flask, flash, render_template, request

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", secrets.token_hex(32))
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024


@app.route("/", methods=["GET", "POST"])
def index():
    selected_file_name = None
    data = None

    if request.method == "POST":
        if "csv_file" not in request.files:
            flash("No se encontró el archivo", "error")
            return render_template("index.html", data=None, selected_file_name=None)

        csv_file = request.files["csv_file"]

        if csv_file.filename == "":
            flash("Selecciona un archivo", "error")
            return render_template("index.html", data=None, selected_file_name=None)

        if not csv_file.filename.lower().endswith(".csv"):
            flash("Solo se permiten archivos .csv", "error")
            return render_template("index.html", data=None, selected_file_name=None)

        try:
            df = pd.read_csv(csv_file)
            if df.empty:
                flash("El archivo CSV está vacío", "error")
                return render_template("index.html", data=None, selected_file_name=None)
            data = df.to_html(
                classes="table table-striped table-bordered", index=False, escape=True
            )
            selected_file_name = csv_file.filename
        except Exception as e:
            flash(f"Error al leer el CSV: {e}", "error")

    return render_template("index.html", data=data, selected_file_name=selected_file_name)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
