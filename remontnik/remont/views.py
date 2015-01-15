# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


# Главная страница приложения
def index(request):
    return HttpResponse(u"Главная страница Remontnik.by")


# Регистрация пользователя
def register(request):
    return HttpResponse(u"Регистрация нового пользователя")


# Личный кабинет пользователя
def profile(request, user_id):
    return HttpResponse(u"Кабинет пользователя %s" % user_id)



