# Generated by Django 3.1 on 2020-08-28 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cochecito', '0002_auto_20200827_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automovil',
            name='anio',
            field=models.IntegerField(verbose_name='año'),
        ),
    ]
