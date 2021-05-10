from django.shortcuts import render
from django.http import HttpResponse # This takes http requests
from . import forms


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

    dictionary["name"] = name
    print(dictionary)
    return render(request, "marvelapp01/characters_search.html", context=dictionary)


def comics(request):
    dictionary = {}
    return render(request, "marvelapp01/comics.html", context=dictionary)

def series(request):
    dictionary = {}
    return render(request, "marvelapp01/series.html", context=dictionary)