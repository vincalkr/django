import json
from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView

from .. import models

def exams_json(request: HttpRequest) -> HttpResponse:
    exams = models.Exam.objects.all()
    
    return HttpResponse(serializers.serialize('json', exams), content_type='application/json')

def exam_detail_json(request: HttpRequest, pk: int) -> HttpResponse:
    exam: models.Exam = get_object_or_404(models.Exam, pk=pk)
    
    return HttpResponse(json.dumps(model_to_dict(exam)), content_type='application/json')

## Test con class based views
class ExamListView(ListView):
    model = models.Exam
    template_name = 'exam-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exams'] = models.Exam.objects.all()
        return context