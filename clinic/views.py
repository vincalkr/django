from django.core import serializers
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from clinic.models import Exam

def index(request: HttpRequest) -> HttpResponse:
    response = HttpResponse()
    response.content = "Hello, world!"
    response.status_code = 200
    return response

def exams(request: HttpRequest) -> HttpResponse:
    exams = Exam.objects.all()
    
    return HttpResponse(serializers.serialize('json', exams), content_type='application/json')