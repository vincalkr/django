from clinic.models import Exam
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request: HttpRequest) -> HttpResponse:
    response = HttpResponse()
    response.content = "Hello, world!"
    response.status_code = 200
    return response

def template_example(request: HttpRequest) -> HttpResponse:
    context = {
        "exams_count": Exam.objects.count(),
        "10exams": Exam.objects.all()[0:10],
    }

    return render(request, 'example.html', context)
