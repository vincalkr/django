import json
from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpRequest, HttpResponse
from clinic.models import Exam, Patient, Reservation

def get_reservations(request: HttpRequest) -> HttpResponse:
    # reservations = Reservation.objects.all()
    patient = Patient(id=1)
    reservations = patient.reservations.all()
    return HttpResponse(serializers.serialize('json', reservations), content_type='application/json')
