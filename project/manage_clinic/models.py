from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthdate = models.DateField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Exam(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()