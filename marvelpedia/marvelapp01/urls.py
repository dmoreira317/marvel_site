from django.conf.urls import url
from django.urls import path
from marvelapp01 import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django import forms

### aqui se generan las rutas relativas

app_name = "marvelapp01"

urlpatterns = [
    # marvelapp pages
    path("characters/", views.characters, name = "characters"),
    path("series/", views.series, name = "series"),
    path("comics/", views.comics, name = "comics"),
    path("characters_search/", views.characters_search, name = "characters_search"),
    path("sign_up_form/", views.sign_up_form, name = "sign_up_form"),
    path("register_results/", views.register_results, name = "register_results"),
    
    # user login, logout and profile
    path("login/", views.login_form, name = "login"),
    path("logout/", views.sign_out, name="signout"),
    path("profile/", views.profile, name="profile"),
    
    # Password change
    path("password_change/", views.change_password, name='password_change'),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(template_name='marvelapp01/password_change_success.html'), name='password_change_done'),
    
]
