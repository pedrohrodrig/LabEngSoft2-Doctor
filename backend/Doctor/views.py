from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Doctor, Evaluation
from .serializers import DoctorSerializer, EvaluationSerializers

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
    
    def list_from_professional_id(self, request, id_user):
        user = request.user
        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        doctor = Doctor.objects.filter(id_user=id_user)
        if not doctor:
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = DoctorSerializer(doctor, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class EvaluationView(ModelViewSet):
    
    serializer_class = EvaluationSerializers
    queryset = Evaluation.objects.all()
    
    def create(self, request):
        serializer = EvaluationSerializers(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        queryset = Evaluation.objects.create(**serializer.validated_data)
        serializer = EvaluationSerializers(queryset)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list_all(self, request):
        queryset = Evaluation.objects.all()
        serializer = EvaluationSerializers(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        queryset = Evaluation.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EvaluationSerializers(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve_by_patient(self, request, pk):
        queryset = Evaluation.objects.filter(patientId=pk)

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EvaluationSerializers(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        queryset = Evaluation.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        queryset.delete()
        serializer = EvaluationSerializers(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)
