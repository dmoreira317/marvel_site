from django import forms
from django.core.exceptions import ValidationError
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate

# Form1 created to take the name in character search page
class Form1(forms.Form):
    name = forms.CharField()

# The sign up takes the Person model as a template, this is a deprecated method in this site, i keep it just as example
# class SignUpForm(ModelForm):
#     class Meta:
#         model = Person
#         fields = "__all__"

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field in ('username', 'email', 'first_name', 'last_name', 'password1', 'password2'):
            self.fields[field].widget.attrs = {'class': 'form-control'}
    
    class Meta:
        model = User
        fields = ['username','email','first_name', 'last_name', 'password1', 'password2']
        
        # If you can modify fields by using attrs, this is an acceptable way
        # widgets = {
        #     'username': forms.CharField(attrs={
        #     'class': 'form-control',
        #     }),
        #     'email': forms.EmailField(attrs={
        #     'class': 'form-control',
      

# Modifying User to be able to update just these fields
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','first_name', 'last_name']
    
# Modifying this class to give it the form-control attrs
class FormChangePassword(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(FormChangePassword, self).__init__(*args, **kwargs)
        for field in ('old_password', 'new_password1', 'new_password2'):
            self.fields[field].widget.attrs = {'class': 'form-control'}