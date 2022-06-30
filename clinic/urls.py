from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('example', views.template_example, name='example'),
    path('reservations/', views.get_reservations, name='reservation_list'),
    path('exams/', views.ExamListView.as_view(), name='exam_list'),
    path('exams/<int:pk>/', views.exam_detail_json, name='exam_detail'),
]