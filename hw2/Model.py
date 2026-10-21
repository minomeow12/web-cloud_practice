from abc import ABC, abstractmethod

class Model(ABC):
  
  @abstractmethod
  def select(self):
    """
    Gets all songs from the database
    """
    pass

  @abstractmethod
  def insert(self, title, artist, url):
    """
    Insert a new song into database
    :param title: string
    :param artist
    :params url: string
    """
    pass
