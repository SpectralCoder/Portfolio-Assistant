from django.urls import path
from django.conf.urls import url
from . import views
from .views import ChatterBotAppView
urlpatterns = [
    path('landing/', ChatterBotAppView.as_view(), name='main'),
    path('', views.index, name='index'),
    path('room', views.room, name='room'),
]