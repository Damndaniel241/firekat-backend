from django.db import models
from .topics import Topic
from accounts.models import CustomUser
from django.utils import  timezone

class Comment(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,related_name="posted_replies")
    content = models.TextField(blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    posted_at = models.DateTimeField(default=timezone.now)
    quoted_comment = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='quoting_comments')
    quoted_topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True, related_name='quoting_topics')
    # image_1 = models.ImageField(upload_to='post_comments/',null=True, blank=True)
    # image_2 = models.ImageField(upload_to='post_comments/',null=True, blank=True)
    # image_3 = models.ImageField(upload_to='post_comments/',null=True, blank=True)
    # image_4 = models.ImageField(upload_to='post_comments/',null=True, blank=True)
    
    
    def save(self, *args, **kwargs):
    # Ensure that either quoted_comment or quoted_topic is set, but not both
        if self.quoted_comment and self.quoted_topic:
            raise ValueError("Cannot quote both a comment and a topic")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user}'s comment in '{self.topic.title}'"


class CommentImage(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_images')
    image = models.ImageField(upload_to='post_comments/', null=True, blank=True)
