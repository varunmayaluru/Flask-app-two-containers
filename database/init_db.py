import sqlite3
import os

# Create a connection to the SQLite database
db_path = os.path.join(os.getcwd(), "data.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the 'data' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        height INTEGER,
        weight INTEGER
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
