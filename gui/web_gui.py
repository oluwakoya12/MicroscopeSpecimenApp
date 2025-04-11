from flask import Flask, render_template_string, request
from app.logic import process_input
from app.database import init_db, get_all_records

app = Flask(__name__)
init_db()

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Microscope Calculator</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f5f7fa;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.1);
            width: 100%;
            max-width: 400px;
            text-align: center;
        }
        input[type="text"],
        input[type="number"] {
            width: 100%;
            padding: 10px;
            margin: 12px 0;
            border: 1px solid #ccc;
            border-radius: 6px;
            font-size: 16px;
        }
        input[type="submit"] {
            background-color: #0179FE;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #005fcc;
        }
        a {
            display: block;
            margin-top: 20px;
            color: #0179FE;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .result {
            margin-top: 20px;
            font-weight: 600;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Microscope Size Calculator</h1>
        <form method="post">
            <input type="text" name="username" placeholder="Username" required>
            <input type="number" name="microscope_size" placeholder="Microscope Size (μm)" step="any" required>
            <input type="submit" value="Calculate">
            <a href="/records">📄 View Saved Records</a>
        </form>
        {% if result %}
        <div class="result">
            Actual Size: {{ result }} μm
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        username = request.form['username']
        microscope_size = float(request.form['microscope_size'])
        result = process_input(username, microscope_size)
    return render_template_string(TEMPLATE, result=result)

@app.route('/records')
def view_records():
    records = get_all_records()
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Saved Records</title>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Poppins', sans-serif;
                background-color: #f5f7fa;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 8px 24px rgba(0,0,0,0.1);
                width: 90%;
                max-width: 700px;
                text-align: center;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }
            th, td {
                padding: 12px 16px;
                border-bottom: 1px solid #ddd;
            }
            th {
                background-color: #0179FE;
                color: white;
                text-align: left;
            }
            tr:hover {
                background-color: #f0f8ff;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                color: #0179FE;
                text-decoration: none;
                font-weight: 500;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>📄 Saved Specimen Records</h2>
            {% if records %}
            <table>
                <tr>
                    <th>Username</th>
                    <th>Microscope Size (μm)</th>
                    <th>Actual Size (μm)</th>
                </tr>
                {% for r in records %}
                <tr>
                    <td>{{ r[0] }}</td>
                    <td>{{ r[1] }}</td>
                    <td>{{ r[2] }}</td>
                </tr>
                {% endfor %}
            </table>
            {% else %}
            <p>No records yet.</p>
            {% endif %}
            <a href="/">← Back to Calculator</a>
        </div>
    </body>
    </html>
    """, records=records)



if __name__ == '__main__':
    app.run(debug=True)
