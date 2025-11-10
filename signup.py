import sqlite3, sys, hashlib

username = sys.argv[1]
email = sys.argv[2]
password = sys.argv[3]

hashed_pw = hashlib.sha256(password.encode()).hexdigest()

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT,
  email TEXT,
  password TEXT
)
''')

c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
          (username, email, hashed_pw))
conn.commit()
conn.close()
