# Generated by Django 5.1 on 2024-10-04 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_topic_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='liked',
        ),
    ]
