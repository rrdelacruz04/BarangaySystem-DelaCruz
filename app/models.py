from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now


class Resident(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)  # Linking to Django's User model
    full_name = models.CharField(max_length=255, blank=True)  # Full name (Optional, can be derived from user fields)
    username = models.CharField(max_length=255, unique=True, blank=True, null=True)  # Custom username
    address = models.CharField(max_length=150)  # Resident's address
    contact_number = models.CharField(max_length=15, unique=True)  # Resident's contact number
    email = models.EmailField(unique=True, blank=True, null=True)  # Resident's email
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when resident is created
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active')  # Active/Inactive status

    def __str__(self):
        # Fallback to a default representation if the user has no names
        return self.full_name if self.full_name else f"{self.user.username}"

    # Automatically populate full_name if not provided
    def save(self, *args, **kwargs):
        if not self.full_name:  # Set full_name if it's not provided
            self.full_name = f"{self.user.first_name} {self.user.last_name}".strip()
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        # Redirect to the Resident's detail view
        return reverse('resident_detail', args=[str(self.id)])


class DocumentRequest(models.Model):
    DOCUMENT_TYPES = [
        ('Certificate of Residency', 'Certificate of Residency'),
        ('Barangay Clearance', 'Barangay Clearance'),
        ('Business Permit', 'Business Permit'),
    ]
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=100, choices=DOCUMENT_TYPES)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.document_type} - {self.resident}"


class IncidentReport(models.Model):
    REPORT_TYPES = [
        ('Fire', 'Fire'),
        ('Crime', 'Crime'),
        ('Medical Emergency', 'Medical Emergency'),
        ('Other', 'Other'),
    ]
    STATUS_CHOICES = [
        ('Reported', 'Reported'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    resident = models.ForeignKey(Resident, on_delete=models.CASCADE, blank=True, null=True)
    report_type = models.CharField(max_length=100, choices=REPORT_TYPES)
    description = models.TextField()
    report_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Reported')

    def __str__(self):
        # Handle case where resident may be null
        resident_name = self.resident.full_name if self.resident else "Anonymous"
        return f"{self.report_type} - {resident_name}"


class Feedback(models.Model):
    STATUS_CHOICES = [
        ('Unread', 'Unread'),
        ('Reviewed', 'Reviewed'),
        ('Resolved', 'Resolved'),
    ]

    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Unread')

    def __str__(self):
        return f"Feedback by {self.resident} - {self.subject}"


class Complaint(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    subject = models.CharField(max_length=150)
    description = models.TextField()
    complaint_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    resolution_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Complaint: {self.subject} by {self.resident}"
