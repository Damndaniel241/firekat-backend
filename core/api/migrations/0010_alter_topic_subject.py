# Generated by Django 5.1 on 2024-09-02 06:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_topic_faculty_alter_topic_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='api.subject'),
        ),
    ]
