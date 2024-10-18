from django.urls import path
from . import views

urlpatterns = [
    path('', views.local_gov, name='local_gov'),
]