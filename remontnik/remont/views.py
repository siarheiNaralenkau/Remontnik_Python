# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from django.template.context import RequestContext
from django.contrib.auth.models import User


# Главная страница приложения
from remont.models import WorkType, JobSuggestion


def index(request):
    top10 = {'top10 masters': 'top10 masters should be displayed here'}
    jobSuggestions = JobSuggestion.objects.order_by("-date_created")[:5]
    return render(request, 'remont/index.html', {"jobSuggestions": jobSuggestions})

# Регистрация пользователя
def register(request):
    return render(request, "remont/register.html", {})


# Личный кабинет пользователя
def profile(request, user_id):
    return HttpResponse(u"Кабинет пользователя %s" % user_id)


# Страница предложения о работе.
def suggest_job(request):
    work_types = WorkType.objects.all()
    # Авторизация еще не реализована
    is_autorized = False
    return render(request, "remont/suggest_job.html", {"is_autorized": is_autorized, "work_types": work_types})


# Сохранение предложения о работе
def suggest_job_save(request):
    contact_person = unicode(request.REQUEST["contactPerson"])
    work_type = request.REQUEST["workType"]
    description = unicode(request.REQUEST["description"])
    phone = request.REQUEST["phone"]
    mail = request.REQUEST["mail"]
    header = request.REQUEST["shortHeader"]

    job_type = WorkType.objects.get(pk=int(work_type))
    job = JobSuggestion(contact_name=contact_person, job_type=job_type, description=description,
                        phone=phone, email=mail, short_header=header)
    job.save()
    # return render(request, "remont/index.html", {})
    return redirect("/remont")

# Регистрация нового пользователя
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





