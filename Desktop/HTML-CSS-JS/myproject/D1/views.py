# chat/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import ChatMessage

# Sign up view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('chat:chatroom')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('chat:chatroom')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Chatroom view
@login_required
def chatroom(request):
    users = User.objects.exclude(id=request.user.id)  # Exclude logged-in user
    return render(request, 'chatroom.html', {'users': users})
