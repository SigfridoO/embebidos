# Generated by Django 5.1.3 on 2024-12-01 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='titulo')),
                ('subtitulo', models.CharField(max_length=100, verbose_name='subtitulo')),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre')),
                ('resumen', models.CharField(max_length=400, verbose_name='resumen')),
                ('contenido', models.CharField(max_length=1000, verbose_name='contenido')),
                ('imagen', models.ImageField(default='', upload_to='pasajes', verbose_name='imagen')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='creado')),
                ('actualizado', models.DateTimeField(auto_now=True, verbose_name='actualizado')),
            ],
            options={
                'verbose_name': 'Memoria',
                'verbose_name_plural': 'Memorias',
                'ordering': ['-creado'],
            },
        ),
    ]
