import sqlite3
from Model import Model

class model(Model):
  def __init__(self):
    """
Initialize the SQLite database and create the playlist table
if it does not already exist.

:return: None
:rtype: None
"""
    with sqlite3.connect("playlist.db") as connection:
      connection.execute("""
        CREATE TABLE IF NOT EXISTS playlist (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          title TEXT NOT NULL,
          artist TEXT NOT NULL,
          url TEXT,
          release_year INTEGER
        )
      """)

  def select(self):
    """
      Return a list of songs.
      Each song contains title, artist, and url
      :return: List of songs.
    """
    with sqlite3.connect('playlist.db') as connection:
      cursor = connection.execute(
        """
          SELECT * FROM playlist
        """
      )
      playlist = cursor.fetchall()
      return playlist
        
      
  def insert(self, title, artist, url, release_year):
    """
        Appends a new list of value representing new song into playlist
        :param title: string
        :param artist: string
        :param url: string
        :param release_year: integer
        :return True
    """ 
    with sqlite3.connect('playlist.db') as connection:
      connection.execute(
        """
          INSERT INTO playlist (title, artist, url, release_year) VALUES (?, ?, ?, ?)""", (title, artist, url, release_year)
          )
      connection.commit()
      return True

    


