from django.db import models

# Create your models here.
class Pet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=5)
    color = models.CharField(max_length=100)

    class Meta:
        ordering = ['created']
