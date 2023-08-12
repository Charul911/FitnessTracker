from django.db import models
from django.contrib.auth.models import User

class Plan(models.Model):
    activity = models.TextField()
    duration = models.IntegerField()
    day = models.CharField(max_length=10)
    time_spent = models.IntegerField(null=True)
    
    def __str__(self):
        return self.activity