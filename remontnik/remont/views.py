# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.template.context import RequestContext


# Главная страница приложения
def index(request):
    top10 = {'top10 masters': 'top10 masters should be displayed here'}
    context = RequestContext(request, top10)
    template = loader.get_template('remont/index.html')
    return HttpResponse(template.render(context))


# Регистрация пользователя
def register(request):
    return HttpResponse(u"Регистрация нового пользователя")


# Личный кабинет пользователя
def profile(request, user_id):
    return HttpResponse(u"Кабинет пользователя %s" % user_id)



