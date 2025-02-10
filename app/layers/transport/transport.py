# capa de transporte/comunicación con otras interfaces o sistemas externos.

import requests
from ...config import config

# comunicación con la REST API.
# este método se encarga de "pegarle" a la API y traer una lista de objetos JSON.
def getAllImages():
    raw_data = requests.get(config.STUDENTS_REST_API_URL).json()

    json_collection = []

    # si la búsqueda no arroja resultados, entonces retornamos una lista vacía de elementos.
    if 'error' in raw_data:
        print("[transport.py]: la búsqueda no arrojó resultados.")
        return json_collection

    for object in raw_data:
        try:
            json_collection.append(object)

        except KeyError: 
            pass

    return json_collection