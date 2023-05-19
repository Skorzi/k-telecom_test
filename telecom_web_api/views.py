from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EquipmentSerializer
from .models import Equipment, Type_Of_Equipment
from django.http import Http404
import string

class GetOrCreateEquip(APIView):
    sn = {'N': [i for i in range(10)], 
          'A': [i for i in string.ascii_uppercase],
          'a': [i for i in string.ascii_lowercase],
          'X': [i for i in string.ascii_lowercase] + [i for i in string.digits],
          'Z': ['-', '_', "@"]
        }
    # Получение всего оборудования
    def get(self, request):
        equip = Equipment.objects.all()
        serializer = EquipmentSerializer(equip, many=True)
        return Response(serializer.data)
    
    # Создание нового оборудования
    def post(self, request):
        serializer = EquipmentSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


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
        pass

    # Удаление записи по id
    def delete(self, request):
        pass

class GetEquipType(APIView):
    # Получить список типов оборудования с query параметрами.
    def get(self, request):
        pass


