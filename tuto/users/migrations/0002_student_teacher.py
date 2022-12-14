# Generated by Django 3.1.3 on 2022-08-14 23:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.CharField(max_length=20, unique=True, verbose_name='Código')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Número de teléfono')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Dirección')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='foto_profesor/', verbose_name='Foto')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='Código')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Número de teléfono')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Dirección')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='foto_estudiante/', verbose_name='Foto')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
            },
        ),
    ]
