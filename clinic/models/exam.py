from django.db import models
from django.urls import reverse
    
class Exam(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def author(self):
        return "vincenzo c."

    def get_absolute_url(self):
        return reverse('exam_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name