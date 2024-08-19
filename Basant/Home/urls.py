from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='WebHome'), #index page
    path('about/', views.about, name='AboutPage'),
]