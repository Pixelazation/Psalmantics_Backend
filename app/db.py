import sqlite3
import os

# Get absolute path to the DB file
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'verses.db')

def get_connection():
  """Returns a new SQLite DB connection."""
  conn = sqlite3.connect(DB_PATH)
  conn.row_factory = sqlite3.Row  # So you can access rows like dicts
  return conn

def get_all_verses():
  conn = get_connection()
  cursor = conn.cursor()
  cursor.execute("""
    SELECT kjv_verses.id AS id, key_english.n AS book, key_english.t AS testament, kjv_verses.c AS chapter, kjv_verses.v AS verse, kjv_verses.t as text
    FROM kjv_verses
    JOIN key_english ON kjv_verses.b = key_english.b
  """)
  results = cursor.fetchall()
  conn.close()
  return [
    {
      'id': row['id'],
      'book': row['book'],
      'testament': row['testament'],
      'chapter': row['chapter'],
      'verse': row['verse'],
      'text': row['text']
    }
    for row in results
  ]

