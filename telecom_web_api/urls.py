from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('equipment/', views.GetOrCreateEquip.as_view()),
    path('equipment/<int:pk>/', views.GetEquipDetail.as_view())
]