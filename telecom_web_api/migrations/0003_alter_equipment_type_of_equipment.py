# Generated by Django 4.2.1 on 2023-05-24 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telecom_web_api', '0002_alter_equipment_type_of_equipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='type_of_equipment',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='telecom_web_api.type_of_equipment'),
        ),
    ]