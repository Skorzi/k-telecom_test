from rest_framework import serializers
from .models import Equipment, Type_Of_Equipment

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class TypeOfEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_Of_Equipment
        fields = '__all__'