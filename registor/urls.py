# registor/urls.py

from django.urls import path
from . import views

app_name = 'registor'

urlpatterns = [
    path('register/', views.register, name='register'),
]
