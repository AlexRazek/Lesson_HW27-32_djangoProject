# Generated by Django 4.0.1 on 2022-05-04 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_age_user_second_name_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='second_name',
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]