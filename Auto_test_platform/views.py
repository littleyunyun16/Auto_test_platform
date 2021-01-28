# -*- coding: utf-8 -*-
__author__ = 'amy'
__date__ = '2020/11/22 15:25'

from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
import logging, os
from lib.execute import create_model


log = logging.getLogger('log')  # 初始化log
def register(request):
    """
    注册
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'user/register.html')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        pswd_again = request.POST.get('pswd-again', '')
        email = request.POST.get('email', '')
        msg = register_info_logic(username, password, pswd_again, email)
        if msg != 'ok':
            log.error('register error：{}'.format(msg))
            return render(request, 'user/register.html', {'error': msg})
        else:
            User.objects.create_user(username=username, password=password, email=email)
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                request.session['user'] = username  # 将session信息记录到浏览器
                user_ = User.objects.get(username=username)
                request.session['user_id'] = user_.id  # 将session信息记录到浏览器
                response = redirect('/index/')
                send_email('注册登录记录', report_id=username, register=True)
                log.info('用户： {} 注册并登录成功！'.format(username))
                request.session.set_expiry(None)  # 关闭浏览器后，session失效
                create_model(user_.id)
                return response

def login_action(request):
    """
    登录
    :param request:
    :return:
    """
    if request.method == 'GET':
        # 把来源的url保存到session中
        request.session['login_from'] = request.META.get('HTTP_REFERER', '/')
        return render(request, 'user/login_action.html')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # response.set_cookie('user', username, 3600)  # 添加浏览器cookie，设置过期时间
            request.session['user'] = username  # 将session信息记录到浏览器
            user_ = User.objects.get(username=username)
            request.session['user_id'] = user_.id  # 将session信息记录到浏览器
            try:
                if request.session['login_from'] == '//':
                    request.session['login_from'] = '/index/'
                elif 'api' in request.session['login_from']:
                    request.session['login_from'] = '/index/'
                elif 'login_action' in request.session['login_from']:
                    request.session['login_from'] = '/index/'
            except KeyError as e:
                request.session['login_from'] = '/index/'
            log.info('---------地址来源-------------> {}'.format(request.session['login_from']))
            response = redirect(request.session['login_from'])
            log.info('用户： {} 登录成功！'.format(username))
            request.session.set_expiry(None)  # 关闭浏览器后，session失效
            create_model(user_.id)
            return response
        else:
            log.error('用户名或密码错误... {} {}'.format(username, password))
            return render(request, 'user/login_action.html', {'error': 'username or password error!'})