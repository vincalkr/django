import json
from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from clinic.models import Exam

def index(request: HttpRequest) -> HttpResponse:
    response = HttpResponse()
    response.content = "Hello, world!"
    response.status_code = 200
    return response

def template_example(request: HttpRequest) -> HttpResponse:
    context = {
        "exams": Exam.objects.all(),
    }

    return render(request, 'example.html', context)

def exams(request: HttpRequest) -> HttpResponse:
    exams = Exam.objects.all()
    
    return HttpResponse(serializers.serialize('json', exams), content_type='application/json')

def exams_detail(request: HttpRequest, id: int) -> HttpResponse:
    exam: Exam = get_object_or_404(Exam, pk=id)
    
    return HttpResponse(json.dumps(model_to_dict(exam)), content_type='application/json')