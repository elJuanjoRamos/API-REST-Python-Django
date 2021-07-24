from persons.models import Person
from persons.serializers import PersonSerializer
from django.http import Http404, response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status



class PersonList(APIView):

    def get(self, request, format=None):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonDetail(APIView):

    def get_person(self, pk):
        try:
            return Person.object.get(pk=pk)
        except Person.DoesNotExist:
            return Http404
    

    def get(self, request, pk, format=None):
        person = self.get_person(pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        person = self.get_person(pk)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        person = self.get_person(pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

