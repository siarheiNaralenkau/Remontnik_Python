from django.conf.urls import patterns, url
from remont import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^(?P<user_id>\d+)/profile/$', views.profile, name='profile'),
)