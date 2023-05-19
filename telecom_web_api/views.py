from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EquipmentSerializer
from .models import Equipment, Type_Of_Equipment
# Create your views here.
class GetOrCreateEquip(APIView):

    # Получение всего оборудования
    def get(self, request):
        equip = Equipment.objects.all()
        serializer = EquipmentSerializer(equip, many=True)
        return Response(serializer.data)
    
    # Создание нового оборудования
    def post(self, request):
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class GetEquipDetail(APIView):
    # Получение записи по id
    def get_equip_by_id(self, pk):
        pass

    # Редактирование записи по id
    def put(self, request):
        pass

    # Удаление записи по id
    def delete(self, request):
        pass

class GetEquipType(APIView):
    # Получить список типов оборудования с query параметрами.
    def get(self, request):
        pass


