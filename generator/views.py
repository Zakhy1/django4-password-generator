import random

from django.shortcuts import render


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    thepassword = ''

    characters = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('Uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))

    if request.GET.get('Special'):
        characters.extend(list('!@#$%^&*()_-+{}[]"/?.><|'))

    if request.GET.get('Numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator/aboutauthor.html')