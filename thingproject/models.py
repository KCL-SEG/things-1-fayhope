from django.db import models

class Thing(models.Model):
  name = models.CharField(max_length=30, unique=True)
  description = models.TextField(blank=True, max_length=120)
  quantity = models.IngegerField()

