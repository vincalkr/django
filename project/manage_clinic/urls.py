from django.urls import path

from . import views

urlpatterns = [
    path('exam/', views.index, name='index'),
    path('exam/detail/<int:exam_id>', views.exam, name='exam'),
]