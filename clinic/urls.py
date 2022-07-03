from django.urls import path
from strawberry.django.views import AsyncGraphQLView
from . import views
from .schema import schema

urlpatterns = [
    path('', views.root.index, name='index'),
    path('example', views.root.template_example, name='example'),
    path('reservations/', views.reservation.get_reservations, name='reservation_list'),
    path('exams/', views.exam.ExamListView.as_view(), name='exam_list'),
    path('exams/<int:pk>/', views.exam.exam_detail_json, name='exam_detail'),
    path("graphql/", AsyncGraphQLView.as_view(schema=schema)),
]