from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name
