from django.db import models
from django.db.models import fields
from rest_framework import serializers
from cars.models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'brand', 'model', 'year']
