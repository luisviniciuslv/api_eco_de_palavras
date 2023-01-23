import sqlite3
from datetime import datetime 

class Repository:
  def __init__(self):
    self.banco = sqlite3.connect('messages.db')
    self.cursor = self.banco.cursor() 
    self.cursor.execute('CREATE TABLE IF NOT EXISTS messages (message text, author text, date text)')

  def create(self, message, author):
    self.cursor.execute('INSERT INTO messages VALUES (?, ?, ?)', (message, author, datetime.now()))
    self.banco.commit()

  def get_random(self):
    self.cursor.execute('SELECT * FROM messages ORDER BY RANDOM() LIMIT 1')
    reponse = self.cursor.fetchone()
    try:
      data = {
        'message': reponse[0],
        'author': reponse[1],
        'date': reponse[2]
      }
    except:
      data = {
        'message': 'No messages found',
        'author': 'No author found',
        'date': 'No date found'
      }
    return data