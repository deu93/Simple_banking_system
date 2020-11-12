import sqlite3

conn = sqlite3.connect('card.s3db')

print(conn.execute('SELECT pin FROM card').fetchall())