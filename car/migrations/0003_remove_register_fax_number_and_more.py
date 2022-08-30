# Generated by Django 4.1 on 2022-08-20 19:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_alter_register_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='fax_number',
        ),
        migrations.AlterField(
            model_name='register',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]