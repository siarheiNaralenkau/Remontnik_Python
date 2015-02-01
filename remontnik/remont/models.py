# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


class WorkCategory(models.Model):
    name = models.CharField(u"Наименование категории работ", max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Категория работ'
        verbose_name_plural = u'Категории работ'


class WorkType(models.Model):
    name = models.CharField(u"Вид работы", max_length=100)
    category = models.ForeignKey(WorkCategory, verbose_name=u"Категория работ")

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


@python_2_unicode_compatible
class JobSuggestion(models.Model):
    class Meta:
        verbose_name = u"Предложение по работе"
        verbose_name_plural = u"Предложения по работе"
    short_header = models.CharField(u"Краткий заголовок заявки", max_length=50, default="",
                                    help_text=u"Краткий заголовок заявки")
    contact_name = models.CharField(u"Контактное лицо", max_length=100, default="")
    job_type = models.ForeignKey(WorkType, verbose_name=u"Вид работ", null=True, default="")
    description = models.TextField(u"Описание работы", default="")
    phone = models.CharField(u"Контактный телефон", max_length=25, default="")
    email = models.EmailField(u"Электронная почта", default="")
    date_created = models.DateTimeField(verbose_name=u"Дата создания", auto_now_add=True)

    def __unicode__(self):
        return "Job info: {0}, {1}, {2}, {3}, {4}".format(self.contact_name, self.job_type, self.description,
                                                         self.phone, self.email)

    def __str__(self):
        return "Job info: {0}, {1}, {2}, {3}, {4}".format(self.contact_name, self.job_type, self.description,
                                                         self.phone, self.email)


