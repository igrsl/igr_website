from django.shortcuts import render
from .models import IndicatorData, SatisfactionData
from django.db.models import Avg, Sum, Case, When, Value, DecimalField

def local_gov(request):
    
    ##############Stability Section Start##################
    stability_indicator = f'% increased in community stability'
    stability_choice = 'Very much'
                                        
    com_stability_choice_values = IndicatorData.objects.filter(indicator__name=stability_indicator, answer_choice_comm_stability=stability_choice, status='approved',). \
                                        values('answer_choice_comm_stability', 'district__name').annotate(avg_value=Avg('indicator_value')). \
                                        order_by('district__name', 'avg_value')
                                        
    stability_districts = []
    stability_choice_district_values = []

    for entry in com_stability_choice_values:
        stability_districts.append(entry['district__name'])
        stability_choice_district_values.append(float(entry['avg_value']))
    
    # Define functions to determine color class and description based on percentage
    def get_color_class(percentage):
        if percentage < 60:
            return "bg-red-500"  # Low
        elif percentage < 70:
            return "bg-yellow-500"  # Medium
        else:
            return "bg-green-500"  # High

    def get_color_description(percentage):
        if percentage < 60:
            return "Low stability"
        elif percentage < 70:
            return "Medium stability"
        else:
            return "High stability"
    
    # Process the percentage values and add color class and color description
    div_data = [
        {
            "district": district,
            "percentage": val,
            "color_class": get_color_class(val),
            "color_description": get_color_description(val),
        }
        for district, val in zip(stability_districts, stability_choice_district_values)
    ]
    # Process the percentage values and add color class
    # div_data = [{'district': district, 'percentage': val, 'color_class': 'bg-red-500' if val < 40 else 'bg-green-500'}
    # for district, val in zip(stability_districts, stability_choice_district_values)
    # ]
    
    
    ##############Stability Section End##################
    
    ##############Audit Recommendation Section Start#########################
    audit_indicator = f'% increase in audit recommendations implemented by the councils'
                                        
    audit_values = IndicatorData.objects.filter(indicator__name=audit_indicator, status='approved',). \
                                    values('district__name').annotate(avg_value=Avg('indicator_value')).order_by('district__name', 'avg_value')
                                        
    audit_districts = []
    audit_district_values = []

    for entry in audit_values:
        audit_districts.append(entry['district__name'])
        audit_district_values.append(float(entry['avg_value']))
        
    # Define functions to determine color class and description based on percentage
    def get_color_class(percentage):
        if percentage < 45:
            return "bg-red-500"  # Low
        elif percentage < 60:
            return "bg-yellow-500"  # Medium
        else:
            return "bg-green-500"  # High

    def get_color_description(percentage):
        if percentage < 45:
            return "Less than 30%"
        elif percentage < 60:
            return "> 30% < 60%"
        else:
            return "> 60%"
    
    # Process the percentage values and add color class and color description
    audit_data = [
        {
            'district': district,
            "percentage": val,
            "color_class": get_color_class(val),
            "color_description": get_color_description(val),
        }
        for district, val in zip(audit_districts, audit_district_values)
    ]
        
    # Process the percentage values and add color class
    # audit_data = [{'district': district, 'percentage': val, 'color_class': 'bg-red-500' if val < 40 else 'bg-green-500'}
    # for district, val in zip(audit_districts, audit_district_values)]
    
    ##############Audit Recommendation Section End#########################
    
    ##############Agricultural Satisfaction Section Start#########################
    agri_satisfaction_indicator = f'Satisfaction with government services in Agriculture​'
                                        
    agri_saf_values = SatisfactionData.objects.filter(indicator__name=agri_satisfaction_indicator, status='approved',). \
                                    values('satisfaction_services').annotate(avg_value=Avg('indicator_value')).order_by('satisfaction_services', 'avg_value')
                                        
    satisfaction_services = []
    satisfaction_services_values = []

    for entry in agri_saf_values:
        satisfaction_services.append(entry['satisfaction_services'])
        satisfaction_services_values.append(float(entry['avg_value']))
        
    # Define functions to determine color class and description based on percentage
    def get_color_class(percentage):
        if percentage < 50:
            return "bg-red-500"  # Low
        elif percentage < 60:
            return "bg-yellow-500"  # Medium
        else:
            return "bg-green-500"  # High

    def get_color_description(percentage):
        if percentage < 50:
            return "Less than 50%"
        elif percentage < 60:
            return "> 50% < 60%"
        else:
            return "> 60%"
    
    # Process the percentage values and add color class and color description
    satisfaction_services_data = [
        {
            'services': service,
            "percentage": val,
            "color_class": get_color_class(val),
            "color_description": get_color_description(val),
        }
        for service, val in zip(satisfaction_services, satisfaction_services_values)
    ]
        
    # Process the percentage values and add color class
    # satisfaction_services_data = [{'services': service, 'percentage': val, 'color_class': 'bg-red-500' if val < 60 else 'bg-green-500'} 
    #                             for service, val in zip(satisfaction_services, satisfaction_services_values)]
    
    ##############Agricultural Satisfaction Section End#########################
    
    context = {
        'stability_districts':stability_districts,
        'div_data': div_data,
        'audit_data':audit_data,
        'satisfaction_services': satisfaction_services,
        'satisfaction_services_data': satisfaction_services_data,
    }
    
    return render(request, 'local_gov.html', context)
