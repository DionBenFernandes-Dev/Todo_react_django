from ast import Str
from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False,blank=True,null=True)

    def __str__(self):
        return self.title