from django.db import models
from django.urls import reverse

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Exam(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('exam_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

class Reservation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='reservations')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient.name + " - " + self.exam.name

    # class Meta: 
    #     verbose_name = 'Reservation'
    #     verbose_name_plural = 'Reservations'