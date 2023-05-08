# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-30 01:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0025_auto_20170730_0208'),
        ('assetmanager', '0002_asset_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='assetDocument',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dashboard.baseModel')),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('document_name', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='assetdocuments/')),
                ('expiry_date', models.DateField()),
                ('proof_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assetmanager.Asset')),
            ],
            bases=('dashboard.basemodel',),
        ),
    ]