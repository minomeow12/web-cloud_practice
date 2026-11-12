from abc import ABC, abstractmethod

class Model(ABC):
  
  @abstractmethod
  def select(self):
    """
    Gets all songs from the database
    return: list of songs
    """
    pass

  @abstractmethod
  def insert(self, title, artist, url, release_year):
    """
    Insert a new song into database
    :param title: string
    :param artist: string
    :param url: string
    :param release_year: integer
    :rtype: bool
    """
    pass
