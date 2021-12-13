from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

class login(models.Model):
    user=models.CharField(max_length=50)
    password=models.CharField(max_length=100)


