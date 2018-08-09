#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django.http import HttpResponseRedirect

def islogin(func):
    def login_fun(request,*args,**kwargs):
        if request.COOKIES.get('uid'):
            return func(request,*args,**kwargs)
        else:
            red = HttpResponseRedirect('/apc/login/2/')
            red.set_cookie('url',request.get_full_path())
            return red
    return login_fun
