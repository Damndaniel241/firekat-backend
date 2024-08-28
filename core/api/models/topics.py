from django.db import models
from .subjects import Subject
from accounts.models import CustomUser
from django.utils import  timezone

from autoslug import AutoSlugField


class Topic(models.Model):
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='title',null=False, unique=True,default=None)
    content = models.TextField(blank=True)
    posted_at = models.DateTimeField(default=timezone.now)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE, related_name='topics')
    author = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True, related_name="owned_topics")



    def __str__(self):
        return self.title

class TopicImage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='topic_images')
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)