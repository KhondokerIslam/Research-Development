from django.db import models

class Inputs(models.Model):
    statement = models.TextField()

    def __str__(self):
        return self.statement
