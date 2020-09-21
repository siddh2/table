from django.db import models

# Create your models here.
class Student(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length=40)
    smarks = models.IntegerField()
    sadd = models.CharField(max_length=64) 