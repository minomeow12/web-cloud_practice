from google.cloud import datastore
from Model import Model

class model(Model):
  def __init__(self):
    """
    Create a client that connect to Google Cloud Database using my credential and initiliaze 
    where playlist store
    :return: None
    :rtype: None
    """
    self.client = datastore.Client()
    self.kind = "HW4Playlist"


  def select(self):
    """
    retrieve songs from Google DataStore
    """
    query = self.client.query(kind=self.kind)
    results = list(query.fetch())
    playlist = []
    for song in results:
      playlist.append((
        song.key.id_or_name,
        song.get("title"),
        song.get("artist"),
        song.get("url"),
        song.get("release_year")
      ))
    return playlist

        
      
  def insert(self, title, artist, url, release_year):
    """
    Appends a new list of value representing new song into playlist
    :param title: string
    :param artist: string
    :param url: string
    :param release_year: integer
    
    """ 
    key = self.client.key(self.kind)
    song = datastore.Entity(key=key)
    song.update({
      "title": title,
      "artist": artist,
      "url": url,
      "release_year": release_year
    })
    self.client.put(song)
    return True
    
    
    


