from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator

class Equipment(models.Model):

    # Использовать функцию валидации?
    def validationSN(self):
        pass

    code = models.CharField(verbose_name='Код типа оборудования',
                            max_length=64, blank=True)
    sn_number = models.CharField(verbose_name='Серийный номер', max_length=10,
                blank=False, unique=True,
                validators=[MinLengthValidator(10), 
                            RegexValidator(regex=r'^[A-Za-z0-9-_@]+$', 
                                message='Использованы недопустимые символы')
                            ]
                )
    
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
            validators=[MinLengthValidator(10), 
            RegexValidator(regex=r'^[NAaXZ]+$', 
                           message='Использованы недопустимые символы')]
            )