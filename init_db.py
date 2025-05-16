import sqlite3

conn = sqlite3.connect('notes.db')
c = conn.cursor()

c.execute("""
CREATE TABLE entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    title TEXT,
    notes TEXT,
    created TIMESTAMP
)
""")

conn.commit()
conn.close()
