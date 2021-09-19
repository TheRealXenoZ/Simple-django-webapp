from django.urls import path

from . import views

urlpatterns = [
    path('weather/', views.weather),
    path('time/', views.time),
    path('contact/', views.contact),
    path('about/', views.about),
    path('diction/', views.diction),
    path('', views.index)
]