from cars.models import Car
from cars.serializers import CarSerializer
from rest_framework import mixins
from rest_framework import generics

class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
