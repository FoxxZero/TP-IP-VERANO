# translator: se refiere a un componente o conjunto de funciones que se utiliza para convertir o "mapear" datos de un formato o estructura a otro. Esta conversión se realiza típicamente cuando se trabaja con diferentes capas de una aplicación, como por ejemplo, entre la capa de datos y la capa de presentación, o entre dos modelos de datos diferentes.

from app.layers.utilities.card import Card

# Usado cuando la información viene de la API, para transformarla en una Card.
def fromRequestIntoCard(object):
    card = Card(
        name=object['name'],  # Nombre del personaje
        gender=object['gender'],  # Género del personaje
        house=object.get('house'),  # Casa (puede no estar presente)
        alternate_names=object.get('alternate_names'), # nombres alternativos
        actor=object.get('actor'),  # Actor (puede no estar presente)
        image=object['image']  # URL de la imagen
    )
    return card


# Usado cuando la información viene del template, para transformarla en una Card antes de guardarla en la base de datos.
def fromTemplateIntoCard(templ): 
    card = Card(
        name=templ.POST.get("name"),
        gender=templ.POST.get("gender"),
        house=templ.POST.get("house"),
        alternate_names=templ.POST.get("alternate_names"),
        actor=templ.POST.get("actor"),
        image=templ.POST.get("image")
    )
    return card


# Cuando la información viene de la base de datos, para transformarla en una Card antes de mostrarla.
def fromRepositoryIntoCard(repo_dict):
    card = Card(
        id=repo_dict.get('id'),
        name=repo_dict.get('name'),
        gender=repo_dict.get('gender'),
        house=repo_dict.get('house'),
        alternate_names='',
        actor=repo_dict.get('actor'),
        image=repo_dict.get('image')
    )
    return card
