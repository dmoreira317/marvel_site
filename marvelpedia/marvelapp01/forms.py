from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from marvelapp01.models import Person

# Form1 created to take the name in character search page
class Form1(forms.Form):
    name = forms.CharField()

# The sign up takes the Person model as a template
# class SignUpForm(ModelForm):
#     class Meta:
#         model = Person
#         fields = "__all__"

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='password1')
    password2 = forms.CharField(label='password2')

    class Meta:
        model = User
        fields = ['username','email','first_name', 'last_name', 'password1', 'password2']
    
    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user

    