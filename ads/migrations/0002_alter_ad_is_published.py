# Generated by Django 4.0.1 on 2022-04-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='is_published',
            field=models.CharField(max_length=20),
        ),
    ]