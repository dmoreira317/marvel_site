from django.shortcuts import render
from django.http import HttpResponse # This takes http requests
from . import forms
from marvelapp01.marvelApiRequests import API_request
from marvelapp01.create_dicts import create_character_dictionary, image_view_generator, character_list_dict
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash
import pprint
import json
import random

# Create your views here.
def vista1(request):
    return HttpResponse("Hola Buenos dias")

def vista2(request):
    dictionary = {}
    API_characters_request_limit = 100
    url = f"https://gateway.marvel.com:443/v1/public/characters?limit={API_characters_request_limit}"
    result = API_request(url)
    # This below works to crate a pretty printed json of all marvel chars
    # with open('all_characters.json', 'w') as f:
    #     f.write(json.dumps(json.loads(result), indent=4, sort_keys=True))
    #     f.close()    

    character_dict = character_list_dict(result)
    dictionary["character_dict"] = character_dict
    
    # generating random characters for the card group
    entry_list = list(character_dict.items())
    print(entry_list)
    random_entry1 = random.choice(entry_list)
    print(random_entry1)
    random_entry2 = random.choice(entry_list)
    random_entry3 = random.choice(entry_list)

    dictionary['random_entry1'] = random_entry1
    dictionary['random_entry2'] = random_entry2
    dictionary['random_entry3'] = random_entry3

    return render(request, "marvelapp01/index.html", context=dictionary)

def characters(request):
    dictionary = {}
    return render(request, "marvelapp01/characters.html", context=dictionary)

def characters_search(request):
    form = forms.Characters() # class defined in forms.py
    dictionary = {"char_search": form}
    
    if request.method == "GET":  # This will retrieve the form fields, in this case, char_search
        form = forms.Characters(request.GET) # creating a variable that receives the GET
        if form.is_valid(): #If request is valid, I pass the value of "name"
            name = form.cleaned_data["name"]
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

# Sign up form
def sign_up_form(request):
    form = forms.SignUpForm() # class defined in forms.py
    dictionary = {"form": form}
    
    if request.method == "POST":  # This will retrieve the form fields, in this case, char_search
        form = forms.SignUpForm(request.POST) # creating a variable that receives the POST
        if form.is_valid(): #If request is valid, I pass the value of "name"
            # name = form.cleaned_data["first_name"]
            
            # print("first", form.cleaned_data["password1"])
            # print("second", form.cleaned_data["password2"])
            
            #check password
            password = form.clean_password2()
            
            # Creating a new User object from the submitted form
            form.save()

            # print("Name = " + name) #print in terminal
            return redirect('register_results/')
        else:
            print("Invalid form request")
            error = form.errors
            print(error)
            dictionary = {
                'error': error
            }    
    else:
        form = forms.SignUpForm()
    
    dictionary = {
            'form': form
            }    
    #print(dictionary["form"])
    return render(request, "marvelapp01/sign_up_form.html", context=dictionary)

# sign up success page   
def register_results(request):
    dictionary = {}
    return render(request, "marvelapp01/register_results.html", context=dictionary)

# Login page
def login_form(request):
    username = 'not logged in'
    user = request.user
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
            return redirect('index')
        else:
            error = form.errors
            print(error)
            dictionary = {
                'error': error
            }
    else:
        form = AuthenticationForm()

    dictionary = {
    'object_list': user,
    'form': form,
    }
          
    return render(request, "marvelapp01/login.html", context=dictionary)

# Sign out page
@login_required(login_url='/pages/login/')
def sign_out(request): # my logout view
    request.session.clear()
    logout(request)
    print("All sessions closed")
    return render(request, "marvelapp01/logout.html")

# User profile update
@login_required(login_url='/pages/login/')
def profile(request):
    user = request.user
    form = forms.UpdateProfileForm(instance=user)
    if request.method == 'POST' :
        form = forms.UpdateProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            print("Profile changes updated correctly")
        else:
            print("Invalid form request")
            error = form.errors
            print(error)
            dictionary = {
                'error': error
            }
    else:
        form = forms.UpdateProfileForm(instance=user)

    dictionary = {
        'object_list': user,
        'form': form,
    }

    return render(request, "marvelapp01/profile.html", context=dictionary)

# Password change page
@login_required(login_url='/pages/login/')
def change_password(request):
    user = request.user
    form = forms.FormChangePassword(user)
    if request.method == 'POST' :
        form = forms.FormChangePassword(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            print("Password changed")
            return redirect('done/')
        else:
            print("Invalid form request")
            error = form.errors
            print(error)
            dictionary = {
                'error': error
            }
    else:
        form = forms.FormChangePassword(user)

    dictionary = {
    'object_list': user,
    'form': form,
    }

    return render(request, "marvelapp01/password_change.html", context=dictionary)


def all_characters(request):
    dictionary = {}
    API_characters_request_limit = 100
    url = f"https://gateway.marvel.com:443/v1/public/characters?limit={API_characters_request_limit}"
    result = API_request(url)
    # This below works to crate a pretty printed json of all marvel chars
    # with open('all_characters.json', 'w') as f:
    #     f.write(json.dumps(json.loads(result), indent=4, sort_keys=True))
    #     f.close()    

    character_dict = character_list_dict(result)
    dictionary["character_dict"] = character_dict

    # img_paths = image_view_generator_all_chars(character_dict, "portrait_uncanny")
    # dictionary["img_paths"] = img_paths
    
    # test api request
    # variable = "avengers"
    # url = f"https://gateway.marvel.com:443/v1/public/characters?series={variable}"
    # result = API_request(url)
    # with open('series.json', 'w') as f:
    #     f.write(json.dumps(json.loads(result), indent=4, sort_keys=True))
    #     f.close() 
    
    print(dictionary)
    return render(request, "marvelapp01/all_characters.html", context=dictionary)
