from django.db import models
from django.contrib.auth.models import User

class Record(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_tags = models.IntegerField(default=0)
    total_accuracy = models.DecimalField(max_digits=13, decimal_places=2, default=0.0)
    accuracy = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

