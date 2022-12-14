# Generated by Django 4.1 on 2022-08-20 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_remove_registerbuyer_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerbuyer',
            name='phone_code',
            field=models.CharField(choices=[('Кыргызстан', 996), ('Казахстан', 7), ('Армения', 374), ('Узбекистан', 998), ('Украина', 380), ('Польша', 48), ('Китай', 86), ('Германия', 49), ('Соединенные Штаты Америки', 1), ('Великобритания', 44)], default=1, max_length=100, verbose_name='Код'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registerprovider',
            name='phone_code',
            field=models.CharField(choices=[('Кыргызстан', 996), ('Казахстан', 7), ('Армения', 374), ('Узбекистан', 998), ('Украина', 380), ('Польша', 48), ('Китай', 86), ('Германия', 49), ('Соединенные Штаты Америки', 1), ('Великобритания', 44)], default=1, max_length=100, verbose_name='Код'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registerbuyer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='registerprovider',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, verbose_name='Номер телефона'),
        ),
    ]
