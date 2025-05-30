import sqlitecloud
import os

from dotenv import load_dotenv

# Get absolute path to the DB file (DB_CONNECTION_STRING from env variables)
load_dotenv()

DB_PATH = os.environ["DB_CONNECTION_STRING"]

def get_connection():
  """Returns a new SQLite DB connection using SQLiteCloud."""
  conn = sqlitecloud.connect(DB_PATH)
  return conn

def get_all_verses():
  conn = get_connection()
  cursor = conn.cursor()
  cursor.execute("""
    SELECT 
      kjv_verses.id AS id, 
      key_english.n AS book, 
      key_english.t AS testament, 
      kjv_verses.c AS chapter, 
      kjv_verses.v AS verse, 
      kjv_verses.t as text
    FROM kjv_verses
    JOIN key_english ON kjv_verses.b = key_english.b
  """)
  
  # Fetch the results (returned as tuples)
  results = cursor.fetchall()
  
  # Get the column names from the cursor description
  if cursor.description is None:
    conn.close()
    return []

  columns = [column[0] for column in cursor.description]
  
  # Convert each row tuple to a dictionary using the column names
  verses = [dict(zip(columns, row)) for row in results]
  
  conn.close()
  return verses
