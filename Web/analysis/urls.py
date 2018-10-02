#!Author:Aydin
#!Date:[[2018-9-27]]
#coding=utf-8

from django.urls import path
from . import views

urlpatterns = [
    # ex: /analysis/
    path('', views.index, name='index'),
    path('one', views.indexOne, name='one'),
    path('two', views.indexTwo, name='two'),
]