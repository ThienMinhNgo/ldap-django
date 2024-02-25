# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .forms import LDAPLoginForm

def ldap_login(request):
    if request.method == 'POST':
        form = LDAPLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate against LDAP
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Bạn đã login.')
                return render(request, 'home.html', {'user': user})
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LDAPLoginForm()

    return render(request, 'ldap_login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('ldap_login')

