from django.db.models import fields
from persons.models import Person
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'lastname', 'phone', 'address']
