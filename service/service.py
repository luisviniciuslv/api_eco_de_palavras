from repo.repository import Repository
from exceptions.invalid_data_except import InvalidDataExcept

class Service:
  def __init__(self):
    self.repository = Repository()

  def create(self, data):
    try:
      message = data['message']
      author = data['author']
      print(type(author))
      self.repository.create(message, author)
    except KeyError:
      raise InvalidDataExcept('Missing required fields')
    
  def get_random(self):
    return self.repository.get_random()