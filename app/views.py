# capa de vista/presentación

from django.shortcuts import redirect, render
from app.layers.services.services import getAllImages # (Gino) Como estaba por default, daba error, se cambio para que traiga la funcion concreta.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from app.layers.services.services import saveFavourite as save_fav_service

def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados: uno de las imágenes de la API y otro de favoritos, ambos en formato Card, y los dibuja en el template 'home.html'.
def home(request):
    images = getAllImages()
    favourite_list = []

    return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })

# función utilizada en el buscador.
def search(request):
    name = request.POST.get('query', '')

    # si el usuario ingresó algo en el buscador, se deben filtrar las imágenes por dicho ingreso.
    if (name != ''):
        images = [img for img in getAllImages() if name.lower() in img.name.lower()]
        favourite_list = []

        return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })
    else:
        return redirect('home')

# función utilizada para filtrar por casa Gryffindor o Slytherin.
def filter_by_house(request):
    house = request.POST.get('house', '')

    if house != '':
        images = [img for img in getAllImages() if img.house == house] # debe traer un listado filtrado de imágenes, según la casa.
        favourite_list = []

        return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })
    else:
        return redirect('home') #volver a la pagina

# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request): #FUNCION QUE DEVUELVE (guille)
    pass

@login_required
def saveFavourite(request): #FUNCION QUE GUARDA (guille)
    if request.method == "POST":
        save_fav_service(request)
    
    return redirect('home')

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    logout(request)
    return redirect('home')