# Generated by Django 5.1.1 on 2024-10-01 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='stu_contact',
            field=models.IntegerField(max_length=30),
        ),
    ]
