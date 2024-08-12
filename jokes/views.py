from django.shortcuts import render
import requests

def home(request):
    return render(request, 'jokes/Landing.html')

baseUrl = 'https://v2.jokeapi.dev/joke/'

joke = setup = delivery = response = None

def data(request, response):
    global joke, setup, delivery
    category = response["category"]
    if response["type"] == "single":
        joke = response["joke"]
    else:
        setup = response["setup"]
        delivery = response["delivery"]

    context = {
        'category': category,
        'joke': joke,
        'setup': setup,
        'delivery': delivery
    }

    return render(request, 'jokes/Display.html', context)

def programming(request):
    response = requests.get(f'{baseUrl}/Programming').json()
    return data(request, response)


def pun(request):
    response = requests.get(f'{baseUrl}/Pun').json()
    return data(request, response)

def dark(request):
    response = requests.get(f'{baseUrl}/Dark').json()
    return data(request, response)


def spooky(request):
    response = requests.get(f'{baseUrl}/Spooky').json()
    return data(request, response)

def miscellaneous(request):
    response = requests.get(f'{baseUrl}/Miscellaneous').json()
    return data(request, response)


def mystery(request):
    response = requests.get(f'{baseUrl}/Any').json()
    return data(request, response)


