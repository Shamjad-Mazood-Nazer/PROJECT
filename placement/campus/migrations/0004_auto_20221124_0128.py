# Generated by Django 3.2.12 on 2022-11-24 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0003_auto_20221123_1450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applydrive',
            old_name='drive_id',
            new_name='drive',
        ),
        migrations.AlterField(
            model_name='studentreg',
            name='email',
            field=models.EmailField(max_length=500, unique=True),
        ),
    ]
