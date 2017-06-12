from django.shortcuts import render, redirect, render_to_response
from django.template.context_processors import csrf
from django.contrib import auth
from django.urls import reverse

from loginsys.forms import UserCreateProfile


def login(request):
    args = dict()
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['error_login'] = "Вы ввели не правильный логин или пороль"
            return render_to_response("loginsys/login.html", args)
    else:
        return render_to_response("loginsys/login.html", args)


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    args = dict()
    args.update(csrf(request))
    args['form'] = UserCreateProfile()
    if request.POST:
        newuser_form = UserCreateProfile(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form

    return render_to_response("loginsys/register.html", args)

