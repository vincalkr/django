from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('example', views.template_example, name='example'),
    path('exams/', views.exams, name='exams'),
    path('exams/<int:pk>/', views.exam_detail, name='exam_detail'),
]