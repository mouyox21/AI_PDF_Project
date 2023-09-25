import sqlite3

# Connect to the database or create it if it doesn't exist
conn = sqlite3.connect('user_credentials.db')
c = conn.cursor()

# Create the users table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT,
        avatar TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
