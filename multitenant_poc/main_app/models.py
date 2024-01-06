from django.db import models

class Perro(models.Model):
  name = models.CharField(max_length=50)