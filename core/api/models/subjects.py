from django.db import models
from .faculties import Faculty

class Subject(models.Model):
    name = models.CharField(max_length=40)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='subjects')
    description = models.TextField(blank=True)
    

    def __str__(self):
        return self.name