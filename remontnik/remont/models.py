# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class WorkCategory(models.Model):
    name = models.CharField(u"Наименование категории работ", max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Категория работ'
        verbose_name_plural = u'Категории работ'


class WorkType(models.Model):
    name = models.CharField(u"Вид работы", max_length=100)
    category = models.ForeignKey(WorkCategory, verbose_name="Категория работ")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Вид работы'
        verbose_name_plural = u'Виды работ'


class UserProfile(models.Model):
    REG_TYPE_CHOICES = (
        (u'client', u'Заказчик'),
        (u'master', u'Исполнитель'),
        (u'seller', u'Продавец'),
    )

    class Meta:
        verbose_name = u"Зарегистрированный пользователь"
        verbose_name_plural = u"Зарегистрированные пользователи"

    user = models.OneToOneField(User)
    reg_type = models.CharField(u"Вид регистрации", choices=REG_TYPE_CHOICES, default='client', max_length=20)
    phone = models.CharField(u"Контактный телефон", max_length=25)


class MasterProfile(UserProfile):
    MASTER_TYPE_CHOICES = (
        (u'one', u'Работаю один'),
        (u'2-3', u'Бригада 2-3 человека'),
        (u'4-10', u'Бригада 4-10 человек'),
        (u'>10', u'Бригада более 10 человек'),
        (u'company', u'Компания')
    )

    CITY_CHOICES = (
        (u'Брест', u'Брест'),
        (u'Витебск', u'Витебск'),
        (u'Гомель', u'Гомель'),
        (u'Гродно', u'Гродно'),
        (u'Минск', u'Минск'),
        (u'Могилев', u'Могилев'),
    )

    master_type = models.CharField(max_length=40, choices=MASTER_TYPE_CHOICES)
    work_types = models.ManyToManyField(WorkType)
    work_location = models.CharField(max_length=30, choices=CITY_CHOICES)
    last_visit = models.DateTimeField()


class WorkPhoto(models.Model):
    photo = models.ImageField()
    master = models.ForeignKey(MasterProfile)



