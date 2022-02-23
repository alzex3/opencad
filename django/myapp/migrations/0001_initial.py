# Generated by Django 4.0.2 on 2022-02-23 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cad_num', models.CharField(max_length=20)),
                ('obj_type', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=250)),
                ('update_date', models.DateField(max_length=10)),
                ('created_date', models.DateField(max_length=10)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=13)),
                ('stamp', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ConstructionObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cad_num', models.CharField(max_length=20)),
                ('obj_type', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=250)),
                ('update_date', models.DateField(max_length=10)),
                ('created_date', models.DateField(max_length=10)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=13)),
                ('stamp', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FlatObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cad_num', models.CharField(max_length=20)),
                ('obj_type', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=250)),
                ('update_date', models.DateField(max_length=10)),
                ('created_date', models.DateField(max_length=10)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=13)),
                ('stamp', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ObjectType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('verbose_name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
        migrations.CreateModel(
            name='ParcelObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cad_num', models.CharField(max_length=20)),
                ('obj_type', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=250)),
                ('update_date', models.DateField(max_length=10)),
                ('created_date', models.DateField(max_length=10)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=13)),
                ('stamp', models.DateField(auto_now_add=True)),
                ('utility', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
