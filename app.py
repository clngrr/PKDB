from flask import Flask, request, render_template, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('notes.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM entries ORDER BY created DESC').fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        url = request.form['url']
        title = request.form['title']
        notes = request.form['notes']
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO entries (url, title, notes, created) VALUES (?, ?, ?, ?)',
            (url, title, notes, datetime.now())
        )
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add.html')
