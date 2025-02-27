# Generated by Django 5.1.4 on 2024-12-30 15:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255)),
                ('username', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('address', models.CharField(max_length=150)),
                ('contact_number', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=20)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IncidentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(choices=[('Fire', 'Fire'), ('Crime', 'Crime'), ('Medical Emergency', 'Medical Emergency'), ('Other', 'Other')], max_length=100)),
                ('description', models.TextField()),
                ('report_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Reported', 'Reported'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved')], default='Reported', max_length=20)),
                ('resident', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.resident')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Unread', 'Unread'), ('Reviewed', 'Reviewed'), ('Resolved', 'Resolved')], default='Unread', max_length=20)),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.resident')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(choices=[('Certificate of Residency', 'Certificate of Residency'), ('Barangay Clearance', 'Barangay Clearance'), ('Business Permit', 'Business Permit')], max_length=100)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=20)),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.resident')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('complaint_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved')], default='Pending', max_length=20)),
                ('resolution_date', models.DateTimeField(blank=True, null=True)),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.resident')),
            ],
        ),
    ]
