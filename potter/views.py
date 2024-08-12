import requests
import random
from django.shortcuts import render
from django.http import HttpRequest

BASE_URL = 'https://potterapi-fedeperin.vercel.app/en/'

def home(request):
    return render(request, 'potter/Landing.html')


                            #THE SPELLS IMPLEMENTATION STARTS HERE
def spells(request: HttpRequest):
    if request.method == 'GET':
        response = randomSpell(request)
    elif request.method == 'POST':
        response = searchedSpell(request)
    else:
        print("Errors Somewhere")

    return response

                #RANDOM SPELL
def randomSpell(request):
            #Constructing the 'Spells' URL
    spellRandom = 'spells/random'
    spellsUrl = f'{BASE_URL}{spellRandom}'
            #Fetching the response
    spellResponse = requests.get(spellsUrl)
    context = None
    if spellResponse.status_code == 200:
        spellResult = spellResponse.json()
        spell = spellResult["spell"]
        use = spellResult["use"]
          #Constructing the context
        context = {'spellName': spell, 'spellUse': use}
    elif spellResponse.status_code == 404:
        print("The Forbidden Error on Random Spell")
    elif spellResponse.status_code == 504:
        print("The Timeout Error on Random Spell")
    else:
        print("Unhandled Spell Error")
    
    return render(request, 'potter/Spells.html', context)

            #SEARCHED SPELL
def searchedSpell(request: HttpRequest):
            #Constructing the 'Spells' URL
    spellSearched = request.POST.get('searchSpell')
    spellQuery = f'spells?search={spellSearched}'   
    postSpellsUrl = f'{BASE_URL}{spellQuery}'     
            #Fetching the response
    spellResponse = requests.get(postSpellsUrl)
    context = None
    if spellResponse.status_code == 200:
        spellResult = spellResponse.json()
        randomSpellIndex = random.randint(0, len(spellResult) - 1)
        spell = spellResult[randomSpellIndex]["spell"]
        use = spellResult[randomSpellIndex]["use"]
            #Constructing the context
        context = {'spellName': spell, 'spellUse': use}
    elif spellResponse.status_code == 404:
        print("The Forbidden Error on Searched Spell")
    elif spellResponse.status_code == 504:
        print("The Timeout Error on Searched Spell")
    else:
        print("Unhandled Spell Error")

    return render(request, 'potter/Spells.html', context)

                            #THE SPELLS IMPLEMENTATION ENDS HERE

def characters(request: HttpRequest):
    if request.method == 'GET':
        response = randomCharacter(request)
    elif request.method == 'POST':
        response = searchedCharacter(request)
    else:
        print("Errors only")
    
    return response

def randomCharacter(request):
            #CHARACTER 
    characterRandom = 'characters/random'
    charactersUrl = f'{BASE_URL}{characterRandom}'
                #CHARACTER RESPONSE
    context = None
    timeout = 10
    characterResponse = requests.get(charactersUrl, timeout=timeout)
    if characterResponse.status_code == 200:
        characterResult = characterResponse.json()
        #randomCharacterIndex = random.randint(0, len(characterResult) - 1)
        name = characterResult["fullName"]
        nick = characterResult["nickname"]
        house = characterResult["hogwartsHouse"]
        children = characterResult["children"]
        if not children:
            children = ['None']
        birthday = characterResult["birthdate"]
        picture = characterResult["image"]
            #Constructing the context
        context = {'randomName': name, 'nick': nick, 'house': house, 'children': children, 'born': birthday, 'pic': picture}
    elif characterResponse.status_code == 404:
        print("The Forbidden Error on Random Character")
    elif characterResponse.status_code == 504:
        print("The Timeout Error on Random Character")
    else:
        print("Unhandled Error")
    
    return render(request, 'potter/Characters.html', context)

def searchedCharacter(request: HttpRequest):
             #CHARACTER
    characterSearched = request.POST.get('searchCharacter')
    CharacterQuery = f'characters?search={characterSearched}'
    postCharactersUrl = f'{BASE_URL}{CharacterQuery}'
                #CHARACTER RESPONSE
    context = None
    timeout = 10
    characterResponse = requests.get(postCharactersUrl, timeout=timeout)
    if characterResponse.status_code == 200:
        characterResult = characterResponse.json()
        randomCharacterIndex = random.randint(0, len(characterResult) - 1)
        name = characterResult[randomCharacterIndex]["fullName"]
        nick = characterResult[randomCharacterIndex]["nickname"]
        house = characterResult[randomCharacterIndex]["hogwartsHouse"]
        children = characterResult[randomCharacterIndex]["children"][0:]
        if not children:
            children = ['None']
        birthday = characterResult[randomCharacterIndex]["birthdate"]
        picture = characterResult[randomCharacterIndex]["image"]
            #Constructing the context
        context = {'randomName': name, 'nick': nick, 'house': house, 'children': children, 'born': birthday, 'pic': picture}
    elif characterResponse.status_code == 404:
        print("The Forbidden Error on Searched Character")
    elif characterResponse.status_code == 504:
        print("The Timeout Error on Searched Character")
    else:
        print("Unhandled Error")
    
    return render(request, 'potter/Characters.html', context)

                            #THE CHARACTERS IMPLEMENTATION ENDS HERE
                            
                            #THE HOUSES IMPLEMENTATION STARTS HERE

def houses(request):
    if request.method == "POST":
        response = searchedHouse(request)
    elif request.method == "GET":
        response = randomHouse(request)
    else:
        print("Houses Errors")

    return response


def randomHouse(request):
                        #HOUSES QUERY
    houseQuery = 'houses/random'
    houseUrl = f'{BASE_URL}{houseQuery}'
        #Fetching the Response
    houseResponse = requests.get(houseUrl)
    if houseResponse.status_code == 200:
        houseResult = houseResponse.json()
        #houseRandomIndex = random.randint(0, len(houseResult) - 1)
        houseName = houseResult["house"]
        houseFounder = houseResult["founder"]
        houseEmoji = houseResult["emoji"]
        houseColours = houseResult["colors"]
        houseAnimal = houseResult["animal"]
            #Constructing the context for 'Houses'
        context = {'houseName': houseName, 'houseFounder': houseFounder, 
                   'houseEmoji': houseEmoji, 'houseColours': houseColours, 'houseAnimal': houseAnimal}
    elif houseResponse.status_code == 404:
        print("The Not Found Error on Random House")
    elif houseResponse.status_code == 504:
        print("The Timeout Error on Random House")
    else:
        # Handle cases where the response is not successful or empty
        print("Error: Could not retrieve valid data from the API")
    return render(request, 'potter/Houses.html', context)

def searchedHouse(request):
            #HOUSE QUERY    
    houseSearched = request.POST.get('searchHouse')
    houseQuery = f'houses?search={houseSearched}'
    houseUrl = f'{BASE_URL}{houseQuery}'
            #FETCHING THE RESPONSE  
    #context = None
    houseResponse = requests.get(houseUrl)
    if houseResponse.status_code == 200:
        houseResult = houseResponse.json()
        houseName = houseResult[0]["house"]
        houseFounder = houseResult[0]["founder"]
        houseEmoji = houseResult[0]["emoji"]
        houseColours = houseResult[0]["colors"]
        houseAnimal = houseResult[0]["animal"]
            #Constructing the context for 'Houses'
        context = {'houseName': houseName, 'houseFounder': houseFounder, 
                   'houseEmoji': houseEmoji, 'houseColours': houseColours, 'houseAnimal': houseAnimal}
    elif houseResponse.status_code == 404:
        print("The Not Found Error on Searched House")
    elif houseResponse.status_code == 504:
        print("The Timeout Error on Searched House")
    else:
        print("Unhandled House Error")
    return render(request, 'potter/Houses.html', context)
                            
                            #THE HOUSES IMPLEMENTATION ENDS HERE

                            #THE BOOKS IMPLEMENTATION STARTS HERE
def books(request):
    if request.method == "POST":
        response = searchedBook(request)
    elif request.method == "GET":
        response = randomBook(request)
    else:
        print("Unhandled Errors on Books")

    return response

def randomBook(request):
    bookQuery = 'books/random'
    bookUrl = f'{BASE_URL}{bookQuery}'
            #FETCHING THE RESPONSE
    bookResponse = requests.get(bookUrl)
    if bookResponse.status_code == 200:
        bookResult = bookResponse.json()
        number = bookResult["number"]
        bookTitle = bookResult["title"]
        release = bookResult["releaseDate"]
        pages = bookResult["pages"]
        description = bookResult["description"]
        cover = bookResult["cover"]
            #Constructing the context for 'Books'
        context = {'number': number, 'title': bookTitle, 'released': release, 'pages': pages, 'description': description, 'cover': cover}
    elif bookResponse.status_code == 404:
        print("The Not Found Error on Searched Book")
    elif bookResponse.status_code == 504:
        print("The Timeout Error on Searched Book")
    else:
        print("Unhandled House Error")
    return render(request, 'potter/Books.html', context)

def searchedBook(request):
    bookSearched = request.POST.get('searchBook')
    bookQuery = f'books?search={bookSearched}'
    bookUrl = f'{BASE_URL}{bookQuery}'
            #FETCHING THE RESPONSE
    bookResponse = requests.get(bookUrl)
    if bookResponse.status_code == 200:
        bookResult = bookResponse.json()[0]
        number = bookResult["number"]
        bookTitle = bookResult["title"]
        release = bookResult["releaseDate"]
        pages = bookResult["pages"]
        description = bookResult["description"]
        cover = bookResult["cover"]
            #Constructing the context for 'Books'
        context = {'number': number, 'title': bookTitle, 'released': release, 'pages': pages, 'description': description, 'cover': cover}
    elif bookResponse.status_code == 404:
        print("The Not Found Error on Searched Book")
    elif bookResponse.status_code == 504:
        print("The Timeout Error on Searched Book")
    else:
        print("Unhandled House Error")
    return render(request, 'potter/Books.html', context)
                            #THE BOOKS IMPLEMENTATION ENDS HERE