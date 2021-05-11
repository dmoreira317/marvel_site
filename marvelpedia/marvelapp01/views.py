from django.shortcuts import render
from django.http import HttpResponse # This takes http requests
from . import forms
from marvelapp01.marvelApiRequests import API_request
from marvelapp01.create_dicts import create_character_dictionary, image_view_generator
import json

# Create your views here.
def vista1(request):
    return HttpResponse("Hola Buenos dias")

def vista2(request):
    dictionary = {}
    return render(request, "marvelapp01/index.html", context=dictionary)

def characters(request):
    dictionary = {}
    return render(request, "marvelapp01/characters.html", context=dictionary)

def characters_search(request):
    char_search = forms.Form1() # class defined in forms.py
    dictionary = {"char_search": char_search}
    
    if request.method == "GET":  # This will retrieve the form fields, in this case, char_search
        char_search1 = forms.Form1(request.GET) # creating a variable that receives the GET
        if char_search1.is_valid(): #If request is valid, I pass the value of "name"
            name = char_search1.cleaned_data["name"]
            print("Name =" + name) #print in terminal
        
    url = f"https://gateway.marvel.com:443/v1/public/characters?name={name}"
    result = API_request(url)
    #print(result)

    character_dict = create_character_dictionary(result)
    dictionary["character_dict"] = character_dict

    img_path = image_view_generator(character_dict["thumbnail"], "portrait_uncanny")
    dictionary["img_path"] = img_path
    
    print(dictionary)
    return render(request, "marvelapp01/characters_search.html", context=dictionary)

def comics(request):
    dictionary = {}
    return render(request, "marvelapp01/comics.html", context=dictionary)

def series(request):
    dictionary = {}
    return render(request, "marvelapp01/series.html", context=dictionary)