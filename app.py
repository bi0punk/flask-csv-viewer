from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'csv_file' not in request.files:
            return redirect(request.url)
        
        csv_file = request.files['csv_file']
        
        if csv_file.filename == '':
            return redirect(request.url)
        
        if csv_file:
            df = pd.read_csv(csv_file)
            return render_template('index.html', data=df.to_html(classes='table table-striped table-bordered', index=False))
    
    return render_template('index.html', data=None)

if __name__ == '__main__':
    app.run(debug=True)
