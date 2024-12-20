# Generated by Django 5.1.4 on 2024-12-16 06:48

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpstracker', '0003_rename_location_perangkat_alter_perangkat_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiwayatPerangkat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('perangkat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gpstracker.perangkat')),
            ],
            options={
                'verbose_name': 'Riwayat Perangkat',
                'verbose_name_plural': 'Riwayat Perangkat',
            },
        ),
    ]
