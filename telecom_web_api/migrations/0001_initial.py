# Generated by Django 4.2.1 on 2023-05-20 13:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type_Of_Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Без названия', max_length=64, verbose_name='Тип оборудования')),
                ('sn_mask', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.RegexValidator(message='Использованы недопустимые символы', regex='^[NAaXZ]+$')], verbose_name='Маска серийного номера')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=64, verbose_name='Код типа оборудования')),
                ('sn_number', models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.RegexValidator(message='Использованы недопустимые символы', regex='^[A-Za-z0-9-_@]+$')], verbose_name='Серийный номер')),
                ('is_deleted', models.BooleanField(default=False)),
                ('type_of_equipment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='telecom_web_api.type_of_equipment')),
            ],
        ),
    ]
