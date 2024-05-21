import requests
from bs4 import BeautifulSoup
import json


# Solicitud get que se almacena en un objeto de tipo request.models.Response que contiene mucho métodos y atributos.
# response = requests.get("https://pypi.org");
# print(response.text); Muestra por consola.

# Las técnicas scraping nos permiten extraer información web para convertirla en datos estructurados con los que trabajar.
# Comprobar el estado de la petición HTTP.
# print(response.status_code);

# Query string: "cadena de consulta" es la parte de la URL que contiene parámetros adicionales que se envían al servidor junto con la solicitud.

# payload = { "q": "tu busqueda" }
# response = requests.get("https://pypi.org", params=payload)

# print(response.url)

# Método de requests para convertir el contenido JSON a un diccionario de Python. Usamos Json Placeholder para aprovechar los datos que devuelve en formato JSON para convertirlos.
# url = "https://jsonplaceholder.typicode.com/posts"
# response = requests.get(url)
# data = response.json()
# print(data)

