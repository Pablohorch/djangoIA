#hello world en python con django

from django.shortcuts import render


def home(request):
    return render(request, 'login.html')



