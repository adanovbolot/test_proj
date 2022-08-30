# Generated by Django 4.1 on 2022-08-20 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0015_remove_registerbuyer_boo_remove_registerprovider_boo_and_more'),
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
            name='score',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='registerprovider',
            name='score',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name=''),
        ),
    ]
