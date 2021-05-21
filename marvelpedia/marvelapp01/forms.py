from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
# from marvelapp01.models import Person

# Form1 created to take the name in character search page
class Form1(forms.Form):
    name = forms.CharField()

# The sign up takes the Person model as a template
# class SignUpForm(ModelForm):
#     class Meta:
#         model = Person
#         fields = "__all__"

class SignUpForm(ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password1 = forms.CharField(label='password1', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','first_name', 'last_name']
    
    def clean_password(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password and password1 and password != password1:
            raise forms.ValidationError("Passwords don't match")
        return password1

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    