# Generated by Django 4.1.3 on 2022-11-27 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Peso', models.FloatField()),
                ('Unidades', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Interes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(1, 'Me interesa adquirir Orellanas'), (2, 'Me interesa cultivar Orellanas')], default=1, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=40)),
                ('Apellidos', models.CharField(max_length=40)),
                ('Edad', models.IntegerField()),
            ],
        ),
    ]
