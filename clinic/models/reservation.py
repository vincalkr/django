from django.db import models
from django.urls import reverse

from .exam import Exam
from .patient import Patient

class Reservation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='reservations')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient.name + " - " + self.exam.name

    # class Meta: 
    #     verbose_name = 'Reservation'
    #     verbose_name_plural = 'Reservations'