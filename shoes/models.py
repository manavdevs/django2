from django.db import models
from django.contrib.auth.models import User

class Shoes(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    quants=models.IntegerField(default=0,null=True, blank=True)
    
    def __str__(self):
        return self.name