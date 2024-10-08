# Generated by Django 5.1 on 2024-09-16 04:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_topic_image_1_topic_image_2_topic_image_3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='image_1',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='image_4',
        ),
        migrations.CreateModel(
            name='TopicImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images/')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_images', to='api.topic')),
            ],
        ),
    ]
