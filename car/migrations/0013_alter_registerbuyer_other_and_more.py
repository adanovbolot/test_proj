# Generated by Django 4.1 on 2022-08-20 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0012_alter_registerbuyer_car_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerbuyer',
            name='other',
            field=models.CharField(blank=True, default=1, max_length=200, verbose_name='Прочее'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registerprovider',
            name='other',
            field=models.CharField(blank=True, default=1, max_length=200, verbose_name='Прочее'),
            preserve_default=False,
        ),
    ]