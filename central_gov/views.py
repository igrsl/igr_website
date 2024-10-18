from django.shortcuts import render

def central_gov(request):
    return render(request, 'central_gov.html')

def budget_allocation(request):
    return render(request, 'budget_allocation.html')
