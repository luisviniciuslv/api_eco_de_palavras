from PyForgeAPI import Routes, Response, Request
from service.service import Service
from exceptions.invalid_data_except import InvalidDataExcept

routes = Routes()

@routes.post('/')
async def main(req: Request, res: Response):
  try: 
    data = req.body.json
    Service().create(data)
    res.status(201)

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