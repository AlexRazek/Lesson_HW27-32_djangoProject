# Generated by Django 4.0.1 on 2022-04-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_ad_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]