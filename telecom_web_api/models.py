from django.db import models

class Equipment(models.Model):
    name = models.CharField(verbose_name='Наименование типа',
                            max_length=64, blank=True)
    sn_number = models.CharField(verbose_name='Серийный номер', max_length=10,
                                blank=False)

class Type_Of_Equipment(models.Model):
    name = models.CharField(verbose_name='Наименование оборудования', 
                            max_length=64, blank=True, default='Без названия')
    sn_mask = models.CharField(verbose_name='Маска серийного номера', 
                               blank=False, max_length=10)