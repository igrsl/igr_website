from django.urls import path
from . import views

urlpatterns = [
    path('', views.cso_media, name='cso_media'),
]