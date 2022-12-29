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

        # crea una instancia de la clase Usuario con los resultados de la consulta
        user = Usuario(results[0][0], results[0][1], results[0][2], results[0][3])

        # guarda en la sesión el objeto user
        request.session['user'] = user.to_json()

        # si el usuario existe en la base de datos redirecciona a la pagina de home
        return redirect('home')

    # si no se envia el username y password redirecciona a la pagina de login
    return render(request, 'login.html')


def home_view(request):
    # Obtener nombre del objecto user de la sesión
    user = json.loads(request.session['user'])

    # validar si el usuario existe en la sesión y que el user.nombre no sea vacio
    if 'user' in request.session and user:

        # consultar la base de datos y obtener todos los habitos filtrando con el id del usuario
        habitosSQL = userRepository.get_habitos(user['id'])

        # crear una lista de habitos
        habitos = []

        # recorrer la lista de habitosSQL y crear un objecto Habitos con los datos de cada habito
        for habito in habitosSQL:
            habitos.append(
                Habitos(habito[0], habito[2], habito[3], habito[4], habito[5], habito[6], habito[7], habito[8]))

        # pasar la lista de habitos a la vista home y username con variable user
        return render(request, 'home.html', {'habitos': habitos, 'username': user})

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
        # guardar en variable el user del request
        user = json.loads(request.session['user'])

        inputIds = ['habito', 'accion', 'mediaActual', 'unidadRegistro', 'unidadMedia', 'unidadRevision', 'proceso']

        # cargar el json de la request GET de habit
        habit = json.loads(request.GET['habit'])
        # con el objecto habit lo mapeas a objecto Habito
        habitodto = Habitos(0, habit['habito'], habit['accion'], habit['mediaActual'], habit['unidadRegistro'],
                            habit['unidadMedia'], habit['unidadRevision'], habit['proceso'])

        # guardar en la base de datos el objecto habitodto
        userRepository.save_habito(user['id'], habitodto)

        # redirecciona a la pagina de home
        return redirect('home')


def delete_habito_view(request):
    # validar si el usuario existe en la sesión
    if 'user' in request.session:
        # guardar en variable el user del request
        user = json.loads(request.session['user'])

        # guardar en variable el id del habito a eliminar
        id = request.GET['id']

        # eliminar el habito de la base de datos
        userRepository.delete_habito(id)

        # redirecciona a la pagina de home
        return redirect('home')
