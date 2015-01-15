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
        ('client', u'Заказчик'),
        ('master', u'Исполнитель'),
        ('seller', u'Продавец'),
    )

    class Meta:
        verbose_name = u"Зарегистрированный пользователь"
        verbose_name_plural = u"Зарегистрированные пользователи"

    user = models.OneToOneField(User)
    reg_type = models.CharField(u"Вид регистрации", choices=REG_TYPE_CHOICES, default='client', max_length=20)
    phone = models.CharField(u"Контактный телефон", max_length=25)



