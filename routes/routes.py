from PyForgeAPI import Routes, Response, Request
from service.service import Service
from exceptions.invalid_data_except import InvalidDataExcept
import time
from typing import Dict

last_request_time: Dict[str, float] = {}
rate_limit = 300
current_time = time.time()

routes = Routes(static_path='static')

@routes.get('/post')
async def index(req: Request, res: Response):
  res.render_page('index.html').status(200).send()

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
    filtro=0
    frase=req.body.json['message']
    print(frase)
    badwords=['<img>','<script>','fuck','fuder','puta','<a>','<center>']
    for palavra in badwords:
      if frase.find(palavra) == -1:
         pass
      else:
         filtro=2
    if filtro == 2:
      res.status(400).json({"error":"contem palavras proibidas" }).send()
      print("post proibido bloqueado")
    else:
      Service().create(data)
      res.send_status(201)

  except InvalidDataExcept as e:
    abre_chave = "{"
    fecha_chave = "}"
    res.status(400).json({"error": e.msg, "required fields": f'{abre_chave}author: example, message: text here{fecha_chave}'}).send() 

@routes.get('/')  
async def main(req: Request, res: Response):
  response = Service().get_random()
  html = f"""
  <head> 
    <meta charset="UTF-8">
  </head>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
  <body> 
    <h1> {response['author']} uma vez disse:</h1>
    <h2> {response['message']} </h2>
    <h3> {response['date']} </h3>
  </body>
  """
  res.html(html).status(200).send()