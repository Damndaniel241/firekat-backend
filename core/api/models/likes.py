from django.db import models
from .topics import Topic
from .comments import Comment
from accounts.models import CustomUser


class Like(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,related_name="liked_posts")
    topic = models.ForeignKey(Topic, null=True, on_delete=models.CASCADE, related_name='likes')
    liked = models.BooleanField(default=False)

    def __str__(self):
        if self.liked:
            return f"{self.user} liked {self.topic.title}"
        else:
            return f"{self.user} unliked {self.topic.title}" 
        

      