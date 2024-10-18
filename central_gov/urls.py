from django.urls import path
from . import views

urlpatterns = [
    path('', views.central_gov, name='central_gov'),
    path('budget-allocation/', views.budget_allocation, name='budget_allocation'),
]