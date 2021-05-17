from django import forms
from django.forms.models import ModelForm
from marvelapp01.models import Person

class Form1(forms.Form):
    name = forms.CharField()


# class SignUpForm(forms.Form):
#     name = forms.CharField()
#     last_name = forms.CharField()
#     username = forms.CharField()
#     password = forms.CharField()
#     email = forms.EmailField()


class SignUpForm(ModelForm):
    class Meta:
        model = Person
        fields = "__all__"



    