from django.contrib import admin
from .models import Resident, DocumentRequest, IncidentReport, Feedback, Complaint

admin.site.register(Resident)
admin.site.register(DocumentRequest)
admin.site.register(IncidentReport)
admin.site.register(Feedback)
admin.site.register(Complaint)

