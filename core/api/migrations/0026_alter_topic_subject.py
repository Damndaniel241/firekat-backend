# Generated by Django 5.1 on 2024-10-11 21:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_alter_topic_faculty_alter_topic_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subject_topics', to='api.subject'),
        ),
    ]
