import strawberry_django
from strawberry import LazyType, auto
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
    
    @strawberry_django.field
    def author(self) -> str:
        return self.author;

@strawberry_django.type(models.Patient, description="Patient type")
class Patient:
    id: auto
    name: auto
    age: auto
    phone: auto
    address: auto
    email: auto
    reservations: List[LazyType["Reservation", __name__]]
    created_at: auto
    updated_at: auto

@strawberry_django.type(models.Reservation, description="Reservation type")
class Reservation:
   id: auto
   patient: LazyType["Patient", __name__]
   exam: Exam
   date: auto
   time: auto
   created_at: auto
   updated_at: auto
