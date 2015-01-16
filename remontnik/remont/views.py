# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.template.context import RequestContext
from django.contrib.auth.models import User


# Главная страница приложения
def index(request):
    top10 = {'top10 masters': 'top10 masters should be displayed here'}
    context = RequestContext(request, top10)
    template = loader.get_template('remont/index.html')
    return HttpResponse(template.render(context))


# Регистрация пользователя
def register(request):
    return render(request, "remont/register.html", {})


# Личный кабинет пользователя
def profile(request, user_id):
    return HttpResponse(u"Кабинет пользователя %s" % user_id)


def create_user(request):
    print "Creating new user..."
    reg_type = request.REQUEST["reg_type"]
    contact_name = request.REQUEST["contact_name"]
    email = request.REQUEST["email"]
    phone = request.REQUEST["phone"]
    password = email
    user = User.objects.create_superuser(email, email, password)
    user.first_name = contact_name
    user.save()
    print "New user was successfully created"

    # TODO redirect to user profile page for editting additional data...





