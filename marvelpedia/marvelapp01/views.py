from django.shortcuts import render
from django.http import HttpResponse # This takes http requests


# Create your views here.
def vista1(request):
    return HttpResponse("Hola Buenos dias")


def vista2(request):
    dictionary = {}
    return render(request, "marvelapp01/index.html", context=dictionary)