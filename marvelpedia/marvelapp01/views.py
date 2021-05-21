from django.forms.utils import ErrorList
from django.shortcuts import render
from django.http import HttpResponse # This takes http requests
from . import forms
from marvelapp01.marvelApiRequests import API_request
from marvelapp01.create_dicts import create_character_dictionary, image_view_generator
from django.http import HttpResponseRedirect
from django.urls import reverse


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

def register_results(request):
    sign_up_form = forms.SignUpForm() # class defined in forms.py
    dictionary = {"sign_up_form": sign_up_form}
    
    if request.method == "POST":  # This will retrieve the form fields, in this case, char_search
        sign_up_form1 = forms.SignUpForm(request.POST) # creating a variable that receives the POST
        if sign_up_form1.is_valid(): #If request is valid, I pass the value of "name"
            name = sign_up_form1.cleaned_data["first_name"]
            last_name = sign_up_form1.cleaned_data["last_name"]
            email = sign_up_form1.cleaned_data["email"]
            username = sign_up_form1.cleaned_data["username"]
            
            print("first", sign_up_form1.cleaned_data["password1"])
            print("second", sign_up_form1.cleaned_data["password2"])
            #check password
            password = sign_up_form1.clean_password()
            
            # Creating a new User object from the submitted form
            sign_up_form1.save()

            # print("Name = " + name) #print in terminal
            # print("Last name = " + last_name)
            # print("Username = " + username)
            # print("Email = " + email)
            # print("pass = " + password)
        else:
            print("Invalid form request")
            error = sign_up_form1.errors
            print(error)
            dictionary = {
                'error': error
            }
            return HttpResponseRedirect(reverse('marvelapp01:sign_up_form'))
    else:
        print("Invalid POST")
        
    
    #print(dictionary["sign_up_form"])
    return render(request, "marvelapp01/register_results.html", context=dictionary)

    
def sign_up_form(request):
    form = forms.SignUpForm()
    dictionary = {
            "form": form,
        }
    return render(request, "marvelapp01/sign_up_form.html", context=dictionary)
