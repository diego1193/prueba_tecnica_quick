# Generated by Django 5.0 on 2023-12-05 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descrition',
            new_name='description',
        ),
    ]
