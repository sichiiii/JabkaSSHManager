from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout


from .forms import SignInForm, SignUpForm, SSHConnectionForm


def sign_in(request):
    return render(request, 'sign_in.html')
    # if request.user.is_authenticated:
    #     if request.method == 'GET':
    #         form = SignInForm()
    #         return render(request, 'sign_in.html', {'form': form})
    #
    #     elif request.method == 'POST':
    #         form = SignInForm(request.POST)
    #
    #         if form.is_valid():
    #             username = form.cleaned_data['username']
    #             password = form.cleaned_data['password']
    #             user = authenticate(request, username=username, password=password)
    #             if user:
    #                 login(request, user)
    #                 return 'True'
    #
    #         messages.error(request, f'Invalid username or password')
    #         return render(request, 'sign_in.html', {'form': form})
    # else:
    #     return render(request, 'error.html', {'error': 'You are logged in'})


@login_required
def sign_out(request):
    logout(request)
    return redirect('sign_in')


def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            form = SignUpForm()
            return render(request, 'sign_up.html', {'form': form})

        elif request.method == 'POST':
            form = SignUpForm(request.POST)

            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user, created = User.objects.get_or_create(username=username, password=password)
                if created:
                    render(request, 'sign_up_success.html')
                else:
                    return render(request, 'error.html', {'error': 'User already exists'})

            return render(request, 'sign_up.html', {'form': form})
    else:
        return render(request, 'error.html', {'error': 'You are already logged in'})


@login_required
def create_ssh_connection(request):
    form = SSHConnectionForm()
    return render(request, 'create_ssh_connection.html', {'form': form})


@login_required
def edit_ssh_connection(request):
    form = SSHConnectionForm()
    return render(request, 'edit_ssh_connection.html', {'form': form})


@login_required
def delete_ssh_connection(request):
    return render(request, 'delete_ssh_connection.html')


@login_required
def connect_ssh_connection(request):
    pass


@login_required
def export_ssh_connections(request):
    pass


@login_required
def import_ssh_connections(request):
    pass
