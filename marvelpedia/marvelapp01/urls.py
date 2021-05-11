from django.conf.urls import url
from django.urls import path
from marvelapp01 import views

### aqui se generan las rutas relativas

app_name = "marvelapp01"

urlpatterns = [
    path("characters/", views.characters, name = "characters"),
    path("series/", views.series, name = "series"),
    path("comics/", views.comics, name = "comics"),
    path("characters_search/", views.characters_search, name = "characters_search"),
    path("sign_up_form/", views.sign_up_form, name = "sign_up_form"),
    path("register_success/", views.register_success, name = "register_success"),

    
]
