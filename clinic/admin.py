from django.contrib import admin

from .models import Patient, Exam, Reservation

admin.site.register(Patient)
admin.site.register(Exam)
admin.site.register(Reservation)

admin.site.index_title = "Amministrazione"
admin.site.site_header = "My Clinic"