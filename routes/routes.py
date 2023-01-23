from PyForgeAPI import Routes, Response, Request
from service.service import Service
from exceptions.invalid_data_except import InvalidDataExcept
import time
from typing import Dict
from datetime import datetime

last_request_time: Dict[str, float] = {}
rate_limit = 300
current_time = time.time()

routes = Routes(static_path='static').cors()

@routes.post('/')
async def main(req: Request, res: Response):
  ip = req._request.client_address[0]
  current_time = time.time()
  if ip in last_request_time:
    elapsed_time = current_time - last_request_time[ip]
    print(elapsed_time)
    print(rate_limit)
    if elapsed_time < rate_limit:
      print('Rate limit exceeded')
      return res.send_status(429)
    
  last_request_time[ip] = current_time
  try: 
    data = req.body.json
    Service().create(data)
    res.send_status(201)
  except InvalidDataExcept as e:
    abre_chave = "{"
    fecha_chave = "}"
    res.status(400).json({"error": e.msg, "required fields": f'{abre_chave}author: example, message: text here{fecha_chave}'}).send() 

@routes.get('/')  
async def main(req: Request, res: Response):
  response = Service().get_random()
  res.json(response).status(200).send()