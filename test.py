import sqlite3

conn = sqlite3.connect('card.s3db')
print(conn.execute("SELECT number FROM card").fetchall())