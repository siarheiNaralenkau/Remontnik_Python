from django.conf.urls import patterns, url
from remont import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^suggest_job/$', views.suggest_job, name='suggest_job'),
    url(r'^(?P<user_id>\d+)/profile/$', views.profile, name='profile'),
    url(r'^create_user/$', views.create_user, name='create_user'),
    url(r'^suggest_job_save/$', views.suggest_job_save, name='suggest_job_save')
)