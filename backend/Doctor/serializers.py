from rest_framework import serializers

from .models import Doctor, Evaluation

class DoctorSerializer(serializers.ModelSerializer): 
    
    class Meta: 
        model = Doctor 
        fields = '__all__'
    
class EvaluationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = "__all__"