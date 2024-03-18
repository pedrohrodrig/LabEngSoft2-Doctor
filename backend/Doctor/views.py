from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Doctor
from .serializers import DoctorSerializer

# Create your views here.
class DoctorView(ModelViewSet): 
    def create(self, request): 
        serializer = DoctorSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        doctor = Doctor.objects.create(**serializer.validate_data)
        doctor_serialized = DoctorSerializer(doctor)

        return Response(doctor_serialized.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk): 
        doctor = Doctor.objects.filter(pk=pk).first()

        if not doctor: 
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = DoctorSerializer(doctor)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def list_all(self, request): 
        doctor_list = Doctor.objects.all()

        if not doctor_list: 
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = DoctorSerializer(doctor_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)