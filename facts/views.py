from django.shortcuts import render
import requests

BASE_URL = 'https://uselessfacts.jsph.pl/api/v2/facts/random'

def jokes(request):
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        data = response.json()
        fact = data["text"]
    elif response.status_code == 404:
        print("The Resource could not be located")
    elif response.status_code == 504:
        print("The server took too long to respond")
    else:
        print(f'Error: {response.status_code}')

    return render(request, 'facts/Main.html', {'fact': fact})
