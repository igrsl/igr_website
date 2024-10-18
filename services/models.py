from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


LANGUAGE = (
        ('', 'Select a gender'),
        ('English', 'English'),
        ('Krio', 'Krio'),
        ('Mende', 'Mende'),
        ('Themne', 'Themne'),
        ('Kono', 'Kono'),
        ('Loko', 'Loko'),
        ('Sherbro', 'Sherbro'),
        ('Limba', 'Limba'),
        ('Fullah', 'Fullah'),
        ('Koranko', 'Koranko'),
        ('Yalunka', 'Yalunka'),
        ('Madingo', 'Madingo'),
        ('Susu', 'Susu'),
        ('Vai', 'Vai'),
        ('Kru', 'Kru'),
        ('Gola', 'Gola'),
        ('Kissi', 'Kissi'),
        ('Other', 'Other'),
)

EDUCATION = (
        ('', 'Select level of education'),
        ('No Schooling', 'No Schooling'),
        ('Informal Schooling', 'Informal Schooling'),
        ('Primary School', 'Primary School'),
        ('Completed Primary School', 'Completed Primary School'),
        ('Secondary School', 'Secondary School'),
        ('Completed Secondary School', 'Completed Secondary School'),
        ('Post-secondary qualifications', 'Post-secondary qualifications, other than university e.g. a diploma or degree from a polytechnic or college'),
        ('Attending University', 'Attending University'),
        ('Completed University', 'Completed University'),
        ('Post-graduate', 'Post-graduate'),
        ('Refused to answer', 'Refused to answer'),
)

SATISFACTORY_LEVEL = (
        ('', 'Select level of satisfaction'),
        ('Very Satisfied', 'Very Satisfied'),
        ('Somewhat Satisfied', 'Somewhat Satisfied'),
        ('Very Dissatisfied', 'Very Dissatisfied'),
        ('Somewhat Dissatisfied', 'Somewhat Dissatisfied'),
        ('Neither', 'Neither'),
)

ACCESS_HEALTH_FACILITIES = (
        ('', 'Select access to health facilities'),
        ('Very easy', 'Very easy'),
        ('Somewhat easy', 'Somewhat easy'),
        ('Somewhat difficult', 'Somewhat difficult'),
        ('Very difficult', 'Very difficult'),
        ("Don't know ", "Don't know "),
)

OCCUPATION = (
        ('', 'Select an occupation'),
        ('Never had a job', 'Never had a job'),
        ('Student', 'Student'),
        ('Housewife / Homemaker', 'Housewife / Homemaker'),
        ('Agriculture / Farming / Fishing / Forestry', 'Agriculture / Farming / Fishing / Forestry'),
        ('Trader / Hawker / Vendor', 'Trader / Hawker / Vendor'),
        ('Retail / Shop', 'Retail / Shop'),
        ('Unskilled manual worker', 'Unskilled manual worker (e.g. cleaner, laborer, domestic help, unskilled manufacturing worker)'),
        ('Artisan or skilled manual worker', 'Artisan or skilled manual worker (e.g. trades like electrician, mechanic, machinist, or skilled manufacturing worker)'),
        ('Clerical or secretarial', 'Clerical or secretarial'),
        ('Supervisor / Foreman / Senior manager', 'Supervisor / Foreman / Senior manager'),
        ('Security services', 'Security services (police, army, private security)'),
        ('Mid-level professional', 'Mid-level professional (e.g. teacher, nurse, mid-level government officer)'),
        ('Upper-level professional', 'Upper-level professional (e.g. banker / finance, doctor, lawyer, engineer, accountant, professor, senior-level government officer)'),
        ('Other', 'Other'),
)

MEDIA_OUTLETS = (
        ('', 'Select a media outlet'),
        ('Notice Board', 'Notice Board'),
        ('Radio', 'Radio'),
        ('Local online news outlet', 'Local online news outlet'),
        ('Print Newspaper', 'Print Newspaper'),
        ('WhatsApp', 'WhatsApp'),
        ('Other Social Media', 'Other Social Media'),
        ('Other', 'Other'),
    )

ANSWER_CHOICE_TRUST = (
        ('', 'Select an answer'),
        ('A lot', 'A lot'),
        ('Somewhat', 'Somewhat'),
        ('Just a little', 'Just a little'),
        ('Not at all', 'Not at all'),
    )

ANSWER_CHOICE_COMM_STABILITY = (
        ('', 'Select an answer'),
        ('Very much', 'Very much'),
        ('Not at all', 'Not at all'),
    )

BRIBERY_SERVICES = (
        ('', 'Select a service'),
        ('Medical services', 'Medical services'),
        ('Public school', 'Public school'),
        ('Identity documents', 'Identity documents'),
    )

AGRI_SATISFACTION = (
        ('', 'Select a service'),
        ('Improved seeds supply', 'Improved seeds supply'),
        ('Training on farming techniques', 'Training on farming techniques'),
        ('Agricultural machines', 'Agricultural machines'),
        ('Fertilizers', 'Fertilizers'),
        ('Processing facilities', 'Processing facilities'),
        ('Advice on farming techniques', 'Advice on farming techniques'),
        ('Financial loans', 'Financial loans'),
    )

GENDER = (
        ('', 'Select a language'),
        ('Male', 'Male'),
        ('Female', 'Female'),
)

class District(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Districts"
    
    def __str__(self):
        return self.name
    
class Chiefdom(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Chiefdoms"
    
    def __str__(self):
        return self.name

class School(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name="School District")
    
    chiefdom = models.CharField(max_length=255)
    
    town_or_village_name = models.CharField(max_length=255)
    
    school_name = models.CharField(max_length=250)
    
    total_girl_students = models.PositiveIntegerField(default=0)
    
    total_boy_students = models.PositiveIntegerField(default=0)
    
    total_female_teachers = models.PositiveIntegerField(default=0)
    
    total_male_teachers = models.PositiveIntegerField(default=0)
    
    total_qualified_teachers = models.PositiveIntegerField(default=0)
    
    total_untrained_teachers = models.PositiveIntegerField(default=0)
    
    total_teachers_with_pin_code = models.PositiveIntegerField(default=0)
    
    total_teachers_without_pin_code = models.PositiveIntegerField(default=0)
    
    shifts_per_day = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name_plural = "Schools"
    
    def __str__(self):
        return self.school_name
        
class ServiceType(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Service Type"
    
    def __str__(self):
        return self.name

class Indicator(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Indicators"
    
    def __str__(self):
        return self.name
    
class IndicatorData(models.Model):
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, null=True, blank=True)
    media_outlets = models.CharField(max_length=100, choices=MEDIA_OUTLETS, blank=True, null=True)
    answer_choice_trust = models.CharField(max_length=100, choices=ANSWER_CHOICE_TRUST, blank=True, null=True)
    answer_choice_comm_stability = models.CharField(max_length=100, choices=ANSWER_CHOICE_COMM_STABILITY, blank=True, null=True)
    bribery_services = models.CharField(max_length=100, choices=BRIBERY_SERVICES, blank=True, null=True)
    indicator_value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=[("pending", "Pending"), ("approved", "Approved")], default="pending")
    date_submitted = models.DateField(auto_now_add=False, default=timezone.now)
    
    class Meta:
        verbose_name_plural = "Indicator Data"
    
    def __str__(self):
        return self.indicator.name


