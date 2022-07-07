from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     print("Save method overridden")
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.name

''' Pre save hook'''
def pre_save_patient(sender, instance, **kwargs):
    print("Pre save patient")

pre_save.connect(pre_save_patient, sender=Patient)