# Generated by Django 5.1 on 2024-10-03 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_comment_image_1_comment_image_2_comment_image_3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='image_1',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='image_4',
        ),
    ]
