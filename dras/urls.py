#!/usr/bin/env python3


from django.urls import path
from . import views


urlpatterns = [
     path('', views.index, name='home'),
     path('information', views.info, name='infomation_center'),
     path('predictions/', views.predict, name='predictions'),
     path('statistics/', views.stats, name='statistics'),
]
