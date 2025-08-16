import sqlite3

conn = sqlite3.connect("habits.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO habits (name, description, frequency, start_date)
VALUES (?, ?, ?, date('now'))
""", ("Morning Run", "Run 3 km every morning", "daily"))

conn.commit()
conn.close()
