# -*- coding: utf-8 -*-
__author__ = 'amy'
__date__ = '2020/11/22 15:25'

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login

def login(request):
    if request.POST:
        username=password=''
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            request.session['user']=username
            response=HttpResponseRedirect('/home/')
            return response
        else:
            return render(request,'login.html',{'error':'用户名或者密码错误'})

    return render(request,'login.html')


def home(request):
    return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')