import strawberry
from typing import List
import strawberry_django
from . import types

@strawberry.type
class Query:
    exam: types.Exam = strawberry_django.field()
    exams: List[ types.Exam] = strawberry_django.field()
    patients: List[ types.Patient] = strawberry_django.field()
    reservations: List[types.Reservation] = strawberry_django.field()

schema = strawberry.Schema(query=Query)
