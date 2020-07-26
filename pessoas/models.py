from django.db import models

# Create your models here.
class Pessoas(models.Model):
    nome = models.CharField(max_length=70, blank=False, default='')
    idade = models.DecimalField(max_digits=4, decimal_places=2)