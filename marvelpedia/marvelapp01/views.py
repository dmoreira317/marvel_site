from django.shortcuts import render
from django.http import HttpResponse # This takes http requests
from . import forms
from marvelapp01.marvelApiRequests import API_request
from marvelapp01.create_dicts import create_character_dictionary, image_view_generator
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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
            
            # print("first", sign_up_form1.cleaned_data["password1"])
            # print("second", sign_up_form1.cleaned_data["password2"])
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
            return redirect('marvelapp01:sign_up_form')
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

def login_form(request):
    username = 'not logged in'
    form = AuthenticationForm()
    dictionary = {
        'form': form
    }
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if username and password:
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        request.session['username'] = username
                        login(request, user)
            print('form and session started')
        else:
            form = AuthenticationForm()
            print('not in session')
        
    return render(request, "marvelapp01/login.html", context=dictionary)

def sign_out(request): # my logout view
    request.session.clear()
    logout(request)
    print("All sessions closed")
    return render(request, "marvelapp01/logout.html")

@login_required(login_url='/pages/login/')
def profile(request):
    user = request.user
    form = forms.SignUpForm()
    if request.method == 'POST' :
        form = forms.SignUpForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        else:
            print("Invalid form request")
            error = form.errors
            print(error)
            dictionary = {
                'error': error
            }
    dictionary = {
    'object_list': user,
    'form': form
    }
    return render(request, "marvelapp01/profile.html", context=dictionary)