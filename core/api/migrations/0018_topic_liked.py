# Generated by Django 5.1 on 2024-10-03 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_remove_comment_image_1_remove_comment_image_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='liked',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
