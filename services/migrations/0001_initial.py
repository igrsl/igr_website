# Generated by Django 5.0.1 on 2024-01-08 05:40

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Districts',
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Indicators',
            },
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Service Type',
            },
        ),
        migrations.CreateModel(
            name='Chiefdom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.district')),
            ],
            options={
                'verbose_name_plural': 'Chiefdoms',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chiefdom', models.CharField(max_length=255)),
                ('town_or_village_name', models.CharField(max_length=255)),
                ('school_name', models.CharField(max_length=250)),
                ('total_girl_students', models.PositiveIntegerField(default=0)),
                ('total_boy_students', models.PositiveIntegerField(default=0)),
                ('total_female_teachers', models.PositiveIntegerField(default=0)),
                ('total_male_teachers', models.PositiveIntegerField(default=0)),
                ('total_qualified_teachers', models.PositiveIntegerField(default=0)),
                ('total_untrained_teachers', models.PositiveIntegerField(default=0)),
                ('total_teachers_with_pin_code', models.PositiveIntegerField(default=0)),
                ('total_teachers_without_pin_code', models.PositiveIntegerField(default=0)),
                ('shifts_per_day', models.PositiveIntegerField(default=0)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.district', verbose_name='School District')),
            ],
            options={
                'verbose_name_plural': 'Schools',
            },
        ),
        migrations.CreateModel(
            name='IndicatorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_outlets', models.CharField(blank=True, choices=[('', 'Select a media outlet'), ('Notice Board', 'Notice Board'), ('Radio', 'Radio'), ('Local online news outlet', 'Local online news outlet'), ('Print Newspaper', 'Print Newspaper'), ('WhatsApp', 'WhatsApp'), ('Other Social Media', 'Other Social Media'), ('Other', 'Other')], max_length=100, null=True)),
                ('answer_choice_trust', models.CharField(blank=True, choices=[('', 'Select an answer'), ('A lot', 'A lot'), ('Somewhat', 'Somewhat'), ('Just a little', 'Just a little'), ('Not at all', 'Not at all')], max_length=100, null=True)),
                ('answer_choice_comm_stability', models.CharField(blank=True, choices=[('', 'Select an answer'), ('Very much', 'Very much'), ('Not at all', 'Not at all')], max_length=100, null=True)),
                ('bribery_services', models.CharField(blank=True, choices=[('', 'Select a service'), ('Medical services', 'Medical services'), ('Public school', 'Public school'), ('Identity documents', 'Identity documents')], max_length=100, null=True)),
                ('indicator_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved')], default='pending', max_length=10)),
                ('date_submitted', models.DateField(default=django.utils.timezone.now)),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.district')),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.indicator')),
                ('service_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.servicetype')),
            ],
            options={
                'verbose_name_plural': 'Indicator Data',
            },
        ),
    ]