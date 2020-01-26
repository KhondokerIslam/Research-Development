from django.db import models

class Input(models.Model):
    statement = models.TextField()
    happy = models.IntegerField(default=0)
    sad = models.IntegerField(default=0)
    stupefied = models.IntegerField(default=0)
    angry = models.IntegerField(default=0)
    others = models.IntegerField(default=0)
    
    def __str__(self):
        return self.statement
