from django.db import models
from datetime import datetime

# Create your models here.


class Tarea(models.Model):
    title = models.CharField(max_length=100,blank=False, unique=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.utcnow())
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
