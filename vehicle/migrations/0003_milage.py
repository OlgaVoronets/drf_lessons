# Generated by Django 5.0.1 on 2024-02-05 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_moto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milage', models.PositiveIntegerField(verbose_name='Пробег')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Год регистрации')),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.car')),
                ('moto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.moto')),
            ],
            options={
                'verbose_name': 'Пробег',
                'verbose_name_plural': 'Пробег',
                'ordering': ('-year',),
            },
        ),
    ]
