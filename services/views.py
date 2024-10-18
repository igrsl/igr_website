from django.shortcuts import render
from .models import School, District, ServiceType, IndicatorData
from django.db.models import Avg, Sum, Case, When, Value, DecimalField
from django.db.models import Count, F, ExpressionWrapper, FloatField
from decimal import Decimal
from datetime import datetime
import json
from django.db.models.functions import ExtractYear
from collections import defaultdict
from django.db.models import Q

def services(request):
    return render(request, 'services.html')
