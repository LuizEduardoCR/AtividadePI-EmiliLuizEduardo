# Generated by Django 5.1.6 on 2025-02-18 17:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='alunos.estado')),
            ],
        ),
    ]
