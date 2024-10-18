from django.urls import path
from . import views

urlpatterns = [
    path('', views.eu_education, name='eu_education'),
]