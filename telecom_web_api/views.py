from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EquipmentSerializer, TypeOfEquipmentSerializer
from .models import Equipment, Type_Of_Equipment
from django.http import Http404
import re

class GetOrCreateEquip(APIView):

    # Получение всего оборудования
    def get(self, request):
        equip = Equipment.objects.filter(is_deleted=False)

        code_query = request.query_params.get('code')
        sn_number_query = request.query_params.get('sn_mask')

        if code_query:
            equip = equip.filter(code=code_query)
        elif sn_number_query:
            equip = equip.filter(sn_number=sn_number_query)
            
        serializer = EquipmentSerializer(equip, many=True)
        return Response(serializer.data)
    
    # Создание нового оборудования
    def post(self, request):
        for equip in request.data:
            equip['type_of_equipment'] = None
        serializer = EquipmentSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class GetEquipDetail(APIView):
    # Получение записи по id
    def get_equip_by_id(self, pk):
        try:
            return Equipment.objects.get(id=pk)
        except Exception:
            raise Http404

    def get(self, request, pk):
        equip_by_id = self.get_equip_by_id(pk)
        serializer = EquipmentSerializer(equip_by_id)
        return Response(serializer.data)

    # Редактирование записи по id
    def put(self, request, pk):
        equip_by_id = self.get_equip_by_id(pk)
        serializer = EquipmentSerializer(equip_by_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # Мягкое удаление записи по id
    def delete(self, request, pk):
        equip_by_id = self.get_equip_by_id(pk)
        equip_by_id.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def restore(self, request, pk):
        equip_by_id = self.get_equip_by_id(pk)
        equip_by_id.restore()
        serializer = EquipmentSerializer(equip_by_id)
        return Response(serializer.data, status=201)

class GetEquipType(APIView):
    # Получить список типов оборудования с query параметрами.
    def get(self, request):
        equip_type = Type_Of_Equipment.objects.all()

        name_query = request.query_params.get('name')
        sn_mask_query = request.query_params.get('sn_mask')

        if name_query:
            equip_type = equip_type.filter(name=name_query)
        elif sn_mask_query:
            equip_type = equip_type.filter(sn_mask=sn_mask_query)

        serializer = TypeOfEquipmentSerializer(equip_type, many=True)
        return Response(serializer.data, status=201)

    def post(self, request):
        serializer = TypeOfEquipmentSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


