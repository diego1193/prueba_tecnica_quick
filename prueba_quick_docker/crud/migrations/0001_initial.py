# Generated by Django 5.0 on 2023-12-05 21:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('nit', models.IntegerField()),
                ('code', models.CharField(max_length=100)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.client')),
            ],
        ),
        migrations.CreateModel(
            name='BillProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.bill')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.product')),
            ],
        ),
    ]
