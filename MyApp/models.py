from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=70)
    age=models.IntegerField()
    contact=models.IntegerField()