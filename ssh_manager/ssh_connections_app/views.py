from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm


def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'sign_in.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return 'True'

        messages.error(request, f'Invalid username or password')
        return render(request, 'sign_in.html', {'form': form})


@login_required
def sign_out(request):
    logout(request)
    return redirect('login')


def sign_up(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'sign_up.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return 'True'

        return render(request, 'sign_up.html', {'form': form})

@login_required
def create_ssh_connection(request):
    pass


@login_required
def edit_ssh_connection(request):
    pass


@login_required
def delete_ssh_connection(request):
    pass


@login_required
def connect_ssh_connection(request):
    pass


@login_required
def export_ssh_connections(request):
    pass


@login_required
def import_ssh_connections(request):
    pass
