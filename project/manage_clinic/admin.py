from django.contrib import admin

from manage_clinic.models import Exam

admin.site.site_header = 'Gestione Clinica'
admin.site.index_title = 'Amministrazione'
admin.site.register(Exam)