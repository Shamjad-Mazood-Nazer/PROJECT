# Generated by Django 3.2.12 on 2022-11-22 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0005_auto_20221122_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='btechstudentdetails',
            name='personalMail',
        ),
        migrations.RemoveField(
            model_name='mcastudentdetails',
            name='personalMail',
        ),
    ]