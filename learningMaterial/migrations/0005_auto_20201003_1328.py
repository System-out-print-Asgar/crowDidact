# Generated by Django 3.1.2 on 2020-10-03 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learningMaterial', '0004_lecturenote_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blurb',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blurb', to='learningMaterial.subject'),
        ),
    ]