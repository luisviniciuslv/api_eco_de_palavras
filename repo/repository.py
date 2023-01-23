import sqlite3
import time 



class Repository:
  def __init__(self):
    self.banco = sqlite3.connect('messages.db')
    self.cursor = self.banco.cursor() 
    self.cursor.execute('CREATE TABLE IF NOT EXISTS messages (message text, author text, date text)')

  def create(self, message, author):
    self.cursor.execute('INSERT INTO messages VALUES (?, ?, ?)', (message, author, time.strftime('%d/%m/%Y %H:%M:%S')))
    self.banco.commit()

  def get_random(self):
    self.cursor.execute('SELECT * FROM messages ORDER BY RANDOM() LIMIT 1')
    reponse = self.cursor.fetchone()
    data = {
      'message': reponse[0],
      'author': reponse[1],
      'date': reponse[2]
    }
    
    return data