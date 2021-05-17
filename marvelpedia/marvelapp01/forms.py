from django import forms

class Form1(forms.Form):
    name = forms.CharField()


class SignUpForm(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()
    


    