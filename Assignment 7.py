# # Implementing Database Operations using python

# Import SQLite Library
import sqlite3

# Connect to a database (creates file if not exists)
conn = sqlite3.connect("my_database.db")

# Create a cursor object
cur = conn.cursor()

# Create a Table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER
)
""")

# Insert Data
cur.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
            ("Gajanan", "gajanan@example.com", 30))

# Save changes
conn.commit()

# Read Data
cur.execute("SELECT * FROM users")
rows = cur.fetchall()

for row in rows:
    print(row)

# Update Data
cur.execute("UPDATE users SET age = ? WHERE name = ?", (31, "Gajanan"))
conn.commit()

#Delete Data
cur.execute("DELETE FROM users WHERE name = ?", ("Gajanan",))
conn.commit()

# Close connection
conn.close()


