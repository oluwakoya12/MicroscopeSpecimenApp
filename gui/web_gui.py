from flask import Flask, render_template, request
from app.logic import process_input
import os
from app.database import init_db, get_all_records

app = Flask(__name__)
init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        username = request.form['username']
        microscope_size = float(request.form['microscope_size'])
        result = process_input(username, microscope_size)
    return render_template('form.html', result=result)

@app.route('/records')
def view_records():
    records = get_all_records()
    return render_template('records.html', records=records)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
