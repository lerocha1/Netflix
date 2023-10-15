# Generated by Django 4.2.6 on 2023-10-15 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0003_rename_seriados_seriado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('usuario', models.CharField(max_length=20, unique=True)),
                ('sexo', models.CharField(choices=[('MASCULIO', 'MAsculino'), ('FEMININO', 'Feminino')], max_length=8)),
            ],
        ),
    ]
