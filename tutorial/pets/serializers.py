from pets.models import Pet
from rest_framework import serializers

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ['id', 'name', 'type', 'age', 'gender', 'color']

"""
class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    age = serializers.CharField()
    gender = serializers.CharField(max_length=5)
    color = serializers.CharField()


    def create(self, valid_data):
        return Pet.objects.create(**valid_data)
    
    def update(self, instance, valid_data):
        instance.name = valid_data.get('name', instance.name)
        instance.type = valid_data.get('type', instance.type)
        instance.age = valid_data.get('age', instance.age)
        instance.gender = valid_data.get('gender', instance.gender)
        instance.color = valid_data.get('color', instance.color)
        instance.save()
        return instance    
"""