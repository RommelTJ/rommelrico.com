from django.conf.urls import patterns, url
from myapps.launchpad import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)

