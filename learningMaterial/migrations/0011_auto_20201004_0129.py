# Generated by Django 3.1.2 on 2020-10-04 05:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningMaterial', '0010_auto_20201003_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blurb',
            name='blurbText',
            field=models.CharField(max_length=50000),
        ),
        migrations.AlterField(
            model_name='lecturenote',
            name='title',
            field=models.CharField(blank=True, default='Note', max_length=80, null=True, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z _]*$', 'Only alphanumeric, spaces, and underscores may be included')]),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=150, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z _]*$', 'Only alphanumeric, spaces, and underscores may be included')]),
        ),
    ]
