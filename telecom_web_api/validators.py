from django.core.exceptions import ValidationError
from .models import Type_Of_Equipment


def validate_sn_mask(value):
    # Для валидации будем составлять маску из серийного номера
    # Если маска будет допустимой, то пробуем найти ее в объектах типа модели
    # Если ее там нету, выдаем ошибку
    
    # Проблема тестового в том, что например серийному номеру вида 0QWER9@123
    # Будет соответствовать как NAAAAXZXXX так и NAAAANZNNN, поэтому наверное 
    # Правильнее думать будет то что первая цифра будет N, а остальные X
    # И тогда будет у него какая-то уникальность 
    
    mask = ""
    special_list = ["-", "_", "@"]
    first_number = True
    
    for character in value:
        if character.isnumeric():
            if first_number:
                mask += "N"
                first_number = False
            else:
                mask += "X"
        elif character.isalpha():
            if character.isupper():
                mask += "A"
            else:
                mask += "a"
        elif character in special_list:
            mask += "Z"
        else:
            raise ValidationError({"msg": "Использованы недопустимые символы"})

    exists = Type_Of_Equipment.objects.filter(sn_mask=mask).exists()
    # type_of_equip = exists
    if not exists:
        raise ValidationError({"msg": "Нету подходящих масок"})
    
    print(mask)

    return mask