import sqlite3
from pathlib import Path

db = Path(__file__).resolve().parent / 'instance' / 'employee.db'
print('DB path:', db)
if not db.exists():
    print('Database file not found.')
else:
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    print('Tables:', cur.fetchall())
    try:
        cur.execute('SELECT * FROM employee')
        rows = cur.fetchall()
        print('Rows count:', len(rows))
        print('Rows sample:', rows[:5])
    except Exception as e:
        print('Query error:', e)
    conn.close()