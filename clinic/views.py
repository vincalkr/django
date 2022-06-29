import json
from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView

from clinic.models import Exam

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

def exams_json(request: HttpRequest) -> HttpResponse:
    exams = Exam.objects.all()
    
    return HttpResponse(serializers.serialize('json', exams), content_type='application/json')

def exam_detail_json(request: HttpRequest, pk: int) -> HttpResponse:
    exam: Exam = get_object_or_404(Exam, pk=pk)
    
    return HttpResponse(json.dumps(model_to_dict(exam)), content_type='application/json')

## Test con class based views
class ExamListView(ListView):
    model = Exam
    template_name = 'exam-list.html'