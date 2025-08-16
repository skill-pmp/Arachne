import sqlite3

# Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect("habits.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create habits table
cursor.execute("""
CREATE TABLE IF NOT EXISTS habits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    frequency TEXT NOT NULL, -- daily, weekly, custom
    start_date TEXT,
    streak INTEGER DEFAULT 0
)
""")

# Create logs table to track completions
cursor.execute("""
CREATE TABLE IF NOT EXISTS habit_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    habit_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    completed INTEGER DEFAULT 0,
    FOREIGN KEY (habit_id) REFERENCES habits(id)
)
""")

conn.commit()
conn.close()
