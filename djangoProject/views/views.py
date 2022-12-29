import json

from django.shortcuts import render, redirect

from djangoProject.Repository import userRepository
from djangoProject.modelos.Habitos import Habitos
from djangoProject.modelos.Usuario import Usuario


# Create your views here.

def login_view(request):
    # guardar en variable el username y password
    username = request.POST.get('username')
    password = request.POST.get('password')

    # validar si el usuario existe en la sesión
    if 'user' in request.session:
        # si existe redirecciona a la pagina de home
        return redirect('home')

    # validar si el usuario existe
    if username and password:

        # usa userRepository para validar si el usuario existe

        results = userRepository.get_user(username, password)
        # muestra los resultados
        print(results)

        # si el usuario no existe en la base de datos redirecciona a la pagina de login con un mensaje de error en el
        # login form
        if not results:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})

        # crea una instancia de la clase Usuario con las variables username y password
        user = Usuario(username, password, False)

        # guarda en la sesión el objeto user
        request.session['user'] = user.to_json()

        # si el usuario existe en la base de datos redirecciona a la pagina de home
        return redirect('home')

    # si no se envia el username y password redirecciona a la pagina de login
    return render(request, 'login.html')


def home_view(request):
    # Obtener nombre del objecto user de la sesión
    username = json.loads(request.session['user'])

    # validar si el usuario existe en la sesión y que el user.nombre no sea vacio
    if 'user' in request.session and username:
        # si existe redirecciona a la pagina de home y envia el nombre del usuario
        return render(request, 'home.html', {'username': username})

    # si no existe redirecciona a la pagina de login
    return redirect('login')


def logout_view(request):
    # validar si el usuario existe en
    if 'user' in request.session:
        # si existe elimina la sesión
        del request.session['user']
    # redirecciona a la pagina de login
    return redirect('login')


def new_habito_view(request):
    # validar si el usuario existe en la sesión
    if 'user' in request.session:
        inputIds = ['habito', 'accion', 'mediaActual', 'unidadRegistro', 'unidadMedia', 'unidadRevision', 'proceso']

        # cargar el json de la request GET de habit
        habit = json.loads(request.GET['habit'])
        # con el objecto habit lo mapeas a objecto Habito
        habitodto = Habitos(habit['habito'], habit['accion'], habit['mediaActual'], habit['unidadRegistro'],  habit['unidadMedia'], habit['unidadRevision'], habit['proceso'])
        # Crea una lista donde solo tenga un elemento de habitoDTO
        habitos = [habitodto]

        # Pasar habit a la vista home para que se muestre en la tabla y mostrar el mensaje de exito
        return render(request, 'home.html', {'habitos': habitos, 'success': 'Hábito creado con éxito'})


