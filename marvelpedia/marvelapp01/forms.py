from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from marvelapp01.models import Person

# Form1 created to take the name in character search page
class Form1(forms.Form):
    name = forms.CharField()

# The sign up takes the Person model as a template
# class SignUpForm(ModelForm):
#     class Meta:
#         model = Person
#         fields = "__all__"

class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']


    