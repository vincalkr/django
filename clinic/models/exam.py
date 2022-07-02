from django.db import models
from django.urls import reverse
    
class Exam(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('exam_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name