import requests
from bs4 import BeautifulSoup
import json


def get_links(url):
    # Obtener todos los enlaces <a> en la página especificada por url.
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return links
    except requests.RequestException as e:
        print(f"Error al acceder a {url}: {e}")
        return []

def get_h1_and_p(url):
    # Obtener todas las etiquetas <h1> y <p> en la página especificada por url.
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        elements = []
        h1_tags = soup.find_all('h1')
        p_tags = soup.find_all('p')
        elements.extend([str(tag) for tag in h1_tags])
        elements.extend([str(tag) for tag in p_tags])
        return elements
    except requests.RequestException as e:
        print(f"Error al acceder a {url}: {e}")
        return []

def crawl_site(start_url):
    # Recorrer el sitio web comenzando desde start_url y almacenar los resultados en un archivo JSON.
    result = {}
    visited = set()
    to_visit = [start_url]

    while to_visit:
        current_url = to_visit.pop(0)
        if current_url not in visited:
            visited.add(current_url)
            print(f"Visitando: {current_url}")
            links = get_links(current_url)
            elements = get_h1_and_p(current_url)
            result[current_url] = elements
            for link in links:
                if link.startswith('https'):
                    to_visit.append(link)
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)


start_url = 'https://www.mercadolibre.com.ar/c/autos-motos-y-otros#menu=categories'
crawl_site(start_url)
