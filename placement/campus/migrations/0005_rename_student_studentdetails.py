# Generated by Django 3.2.12 on 2022-11-14 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0004_auto_20221113_2327'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='StudentDetails',
        ),
    ]
