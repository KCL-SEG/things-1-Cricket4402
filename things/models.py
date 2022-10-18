from enum import unique
from wsgiref.validate import validator
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120, unique=False, blank=True)
    quantity = models.IntegerField(unique=False,
                                   validators=[MaxValueValidator(100, "Can't be over 100"),
                                              MinValueValidator(0, "Can't be below 0")])