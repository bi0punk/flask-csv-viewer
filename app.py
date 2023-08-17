from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_file_name = None
    
    if request.method == 'POST':
        if 'csv_file' not in request.files:
            return redirect(request.url)
        
        csv_file = request.files['csv_file']
        
        if csv_file.filename == '':
            return redirect(request.url)
        
        selected_file_name = csv_file.filename
        
        if csv_file:
            df = pd.read_csv(csv_file, skiprows=10)
            return render_template('index.html', data=df.to_html(classes='table table-striped table-bordered', index=False), selected_file_name=selected_file_name)
    
    return render_template('index.html', data=None, selected_file_name=selected_file_name)

if __name__ == '__main__':
    app.run(debug=True)
