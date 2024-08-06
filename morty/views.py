from django.shortcuts import render
import requests
import random

BASE_URL = 'https://rickandmortyapi.com/api/'

def home(request):
  return render(request, 'morty/Landing.html')


def characterMain(request):
  if request.method == 'POST':
    response = searchedCharacter(request)
  elif request.method == 'GET':
    response = randomCharacter(request)
  else:
    response = print("errors")

  return response

def locationMain(request):
  if request.method == 'POST':
    response = searchedLocation(request)
  elif request.method == 'GET':
    response = randomLocation(request)
  else:
    response = print("errors")

  return response
     #CHARACTERS ENDPOINT
def searchedCharacter(request):
  charSearch = request.POST.get('searchCharacter', '1')
  characterConst = f'character/{charSearch}'
  characterUrl = f'{BASE_URL}{characterConst}'

  context = None
  characterQuery = requests.get(characterUrl)
  if characterQuery.status_code == 200:
    response = characterQuery.json()
    characterName = response["name"]
    status = response["status"]
    gender = response["gender"]
    species = response["species"]
    origin = response["origin"]["name"]
    pic = response["image"]

    context = {
        'name': characterName,
        'status': status,
        'gender': gender,
        'species': species,
        'origin': origin,
        'picture': pic
    }
  elif characterQuery.status_code == 404:
    print("The Resource could not be located")
  elif characterQuery.status_code == 504:
    print("The server took too long to respond")
  else:
    print(f'Error: {characterQuery.status_code}')
  return render(request, 'morty/Characters.html', context)


def randomCharacter(request):
  randomChar = f'{BASE_URL}character'
  randomCharQuery = requests.get(randomChar)
  context = None
  if randomCharQuery.status_code == 200:
    response = randomCharQuery.json()["results"]
    randomCharIndex = random.randint(0, len(response) - 1)
    characterName = response[randomCharIndex]["name"]
    status = response[randomCharIndex]["status"]
    gender = response[randomCharIndex]["gender"]
    species = response[randomCharIndex]["species"]
    origin = response[randomCharIndex]["origin"]["name"]
    pic = response[randomCharIndex]["image"]

    context = {
        'name': characterName,
        'status': status,
        'gender': gender,
        'species': species,
        'origin': origin,
        'picture': pic
    }
  elif randomCharQuery.status_code == 404:
    print("The Resource could not be located")
  elif randomCharQuery.status_code == 504:
    print("The server took too long to respond")
  else:
    print(f'Error: {randomCharQuery.status_code}')
  return render(request, 'morty/Characters.html', context)


    #LOCATIONS ENDPOINT  
def searchedLocation(request):
  locSearch = request.POST.get('searchLocation', '1')
  locConst = f'location/{locSearch}'
  locationURL = f'{BASE_URL}{locConst}'

  context = None
  locationQuery = requests.get(locationURL)
  if locationQuery.status_code == 200:
    locationResponse = locationQuery.json()
    locationName = locationResponse["name"]
    dimension = locationResponse["dimension"]
    type = locationResponse["type"]

    context = {
        'locationName': locationName,
        'dimension': dimension,
        'type': type
    }
  elif locationQuery.status_code == 404:
    print("The Resource could not be located")
  elif locationQuery.status_code == 504:
    print("The server took too long to respond")
  else:
    print(f'Error: {locationQuery.status_code}')
  return render(request, 'morty/Locations.html', context)


def randomLocation(request):
  randLoc = f'{BASE_URL}location'
  randLocQuery = requests.get(randLoc)

  context = None
  if randLocQuery.status_code == 200:
    locationResponse = randLocQuery.json()["results"]
    randomLocaIndex = random.randint(0, len(locationResponse) - 1)
    locationName = locationResponse[randomLocaIndex]["name"]
    dimension = locationResponse[randomLocaIndex]["dimension"]
    type = locationResponse[randomLocaIndex]["type"]

    context = {
        'locationName': locationName,
        'dimension': dimension,
        'type': type  
    }
  elif randLocQuery.status_code == 404:
    print("The Resource could not be located")
  elif randLocQuery.status_code == 504:
    print("The server took too long to respond")
  else:
    print(f'Error: {randLocQuery.status_code}')

  return render(request, 'morty/Locations.html', context)
