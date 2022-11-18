# Generated by Django 3.2.12 on 2022-11-18 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0006_auto_20221118_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcastudentdetails',
            name='branch',
            field=models.CharField(choices=[('mca', 'MCA'), ('intmca', 'INT MCA')], max_length=50),
        ),
        migrations.AlterField(
            model_name='mcastudentdetails',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6),
        ),
    ]
