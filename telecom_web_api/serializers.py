from rest_framework import serializers
from .models import Equipment, Type_Of_Equipment
from .validators import validate_sn_mask

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

    def validate(self, args):
        validate_sn_mask(args['sn_number'])
        return super().validate(args)

class TypeOfEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_Of_Equipment
        fields = '__all__'