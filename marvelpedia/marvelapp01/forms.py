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
    password1 = forms.CharField(label='password1')
    password2 = forms.CharField(label='password2')

    class Meta:
        model = User
        fields = ['username','email','first_name', 'last_name', 'password1', 'password2']
    
    # parsing both incoming passwords
    def clean_password(self):
        password1 = self.cleaned_data.get("password1")
        print('password1: ', password1)
        password2 = self.cleaned_data.get("password2")
        print('password2: ', password2)
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user

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