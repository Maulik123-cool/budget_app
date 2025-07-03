from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                description TEXT,
                amount REAL,
                type TEXT,
                category TEXT
            )
        ''')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        desc = request.form['description']
        amount = float(request.form['amount'])
        t_type = request.form['type']
        category = request.form['category']
        with sqlite3.connect('database.db') as conn:
            conn.execute("INSERT INTO transactions (description, amount, type, category) VALUES (?, ?, ?, ?)",
                         (desc, amount, t_type, category))
            conn.commit()

    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM transactions")
        transactions = cur.fetchall()
    return render_template('dashboard.html', transactions=transactions)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)