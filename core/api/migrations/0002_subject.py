# Generated by Django 5.1 on 2024-08-28 00:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='api.faculty')),
            ],
        ),
    ]
