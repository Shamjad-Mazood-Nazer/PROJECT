# Generated by Django 3.2.12 on 2022-11-18 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0007_auto_20221118_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='btechstudentdetails',
            name='branch',
            field=models.CharField(choices=[('it', 'information_technology'), ('me', 'mech'), ('ce', 'civil'), ('eee', 'eee'), ('ece', 'ece'), ('ch', 'chemical'), ('cse', 'cse')], max_length=50),
        ),
        migrations.AlterField(
            model_name='btechstudentdetails',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=6),
        ),
    ]