from rest_framework import serializers
from .models import Equipment, Type_Of_Equipment
from .validators import validate_sn_mask

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'
        extra_kwargs = {
            'type_of_equipment': {'required': False}
        }

    def validate(self, args):
        equipment_type_instance = validate_sn_mask(args['sn_number'])
        args['type_of_equipment'] = equipment_type_instance
        return super().validate(args)

class TypeOfEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type_Of_Equipment
        fields = '__all__'