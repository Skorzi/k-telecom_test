from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class GetOrCreateEquip(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"})
    
    def post(self, request):
        #create a new equip
        pass

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


