import strawberry_django
from strawberry import auto
from typing import List
from . import models

@strawberry_django.type(models.Exam, description="Exam type")
class Exam:
    id: auto
    name: auto
    description: auto
    price: auto
    created_at: auto
    updated_at: auto

@strawberry_django.type(models.Patient, description="Patient type")
class Patient:
    id: auto
    name: auto
    age: auto
    phone: auto
    address: auto
    email: auto
    created_at: auto
    updated_at: auto

@strawberry_django.type(models.Reservation, description="Reservation type")
class Reservation:
   id: auto
   patient: Patient
   exam: Exam
   date: auto
   time: auto
   created_at: auto
   updated_at: auto
