# Generated by Django 4.1 on 2022-08-20 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0013_alter_registerbuyer_other_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerbuyer',
            name='boo',
            field=models.BooleanField(default=False, verbose_name=''),
        ),
        migrations.AddField(
            model_name='registerprovider',
            name='boo',
            field=models.BooleanField(default=False, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='registerbuyer',
            name='other',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Прочее'),
        ),
        migrations.AlterField(
            model_name='registerprovider',
            name='other',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Прочее'),
        ),
    ]