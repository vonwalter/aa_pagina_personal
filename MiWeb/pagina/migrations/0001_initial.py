# Generated by Django 5.0.6 on 2024-07-02 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('foto_de_fondo', models.ImageField(upload_to='fondo/')),
                ('mi_foto', models.ImageField(upload_to='fotos/')),
                ('soy_1', models.CharField(max_length=100)),
                ('soy_2', models.CharField(max_length=100)),
                ('soy_3', models.CharField(max_length=100)),
            ],
        ),
    ]
