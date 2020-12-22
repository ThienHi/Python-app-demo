from django.urls import path
from . import views

app_name = 'menu'
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('list/', views.save, name='save'),
]
