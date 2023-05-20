from django.db import models
from django.core.validators import MinLengthValidator

class Equipment(models.Model):
    code = models.CharField(verbose_name='Код типа оборудования',
                            max_length=64, blank=True)
    sn_number = models.CharField(verbose_name='Серийный номер', max_length=10,
                blank=False, validators=[MinLengthValidator(10)], unique=True)
    
    is_deleted = models.BooleanField(default=False)
    
    # Заготовки для мягкого удаления.
    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

class Type_Of_Equipment(models.Model):
    name = models.CharField(verbose_name='Тип оборудования', max_length=64, 
                            blank=True, default='Без названия')
    sn_mask = models.CharField(verbose_name='Маска серийного номера', 
                                blank=False, max_length=10, 
                                validators=[MinLengthValidator(10)])