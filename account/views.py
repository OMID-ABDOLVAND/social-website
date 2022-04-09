from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .form import LoginForm
from django.contrib.auth.decorators import login_required


# Create your views here.
'''
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']  # user_name = request.POST['username' / 'password']
            pass_word = form.cleaned_data['password']
            user = authenticate(request, username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    HttpResponse('disable account')
            else:
                HttpResponse('invalid login')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})
'''


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
