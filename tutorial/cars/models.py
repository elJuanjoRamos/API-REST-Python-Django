from django.db import models

class Car(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    
    class Meta:
        ordering = ['created']
