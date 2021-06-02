from django import forms
from django.shortcuts import render, redirect

class LoginForm(forms.Form):
    username = forms.CharField(label=("Username"), required=True)
    password = forms.CharField(label=("Username"), widget=forms.PasswordInput, required=True)

# First Sessions Attempt
# def session_demo(request):
#     username = None #Default value
#     form_login = LoginForm()
#     if request.method == 'GET':
#         if 'action' in request.GET:
#             action = request.GET.get('action')
#             if action == 'logout':
#                 if request.session.has_key('username'):
#                     request.session.flush()
#                 return redirect('marvelapp01/index.html')

#         if 'username' in request.session:
#             username = request.session['username']
#             print(request.session.get_expiry_age()) #Session lifetime in seconds (from nov)
#             print(
#                 request.session.get_expiry_date()) # datetime.datetime object which represents the moment in time at which

#     elif request.method == 'POST':
#         form_login = LoginForm(request.POST)
#         if form_login.is_valid():
#             username = form_login.cleaned_data['username']
#             password = form_login.cleaned_data['password']
#             if username.strip() == 'diego' and password.strip() == 'secret':
#                 request.session['username'] = username
#             else:
#                     username = None
    
#     return render(request, 'sessions.html', {
#         'demo_title': 'sessions in DJango',
#         'form': form_login,
#         'username': username,
#         })

