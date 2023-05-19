from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EquipmentSerializer
from .models import Equipment, Type_Of_Equipment
# Create your views here.
class GetOrCreateEquip(APIView):
    def get_object(self, request, pk):
        pass

    def get(self, request):
        equip = Equipment.objects.all()
        serializer = EquipmentSerializer(equip, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        #create a new equip
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request):
        #на редактирование записи по id
        pass

    def delete(self, request):
        #на удаление записи по id
        pass

class GetEquipType(APIView):
    def get(self, request):
        # Получить список типов оборудования с query параметрами.
        pass


