from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidators
from djang.core.exceptions import ValidationError

def validate_quantity_range(value):
  if value < 0 or value > 100:
    raise ValidationError("Quantity must be between 0 to 100")


class Thing(models.Model):
  name = models.CharField(max_length=30, unique=True)
  description = models.TextField(blank=True, max_length=120)
  quantity = models.IngegerField()

  def __str__(self):
    return self.name 








