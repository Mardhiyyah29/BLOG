import sqlite3

# open your DB
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

# add slug columns if they don't exist
try:
    cursor.execute("ALTER TABLE blogs_blogs ADD COLUMN slug varchar(100);")
except Exception as e:
    print("Article slug exists:", e)

try:
    cursor.execute("ALTER TABLE blogs_category ADD COLUMN slug varchar(100);")
except Exception as e:
    print("Category slug exists:", e)

conn.commit()
conn.close()