from django.db import models
from .comments import Comment
from accounts.models import CustomUser


class CommentLike(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,related_name="liked_comments")
    comment = models.ForeignKey(Comment, null=True, on_delete=models.CASCADE, related_name='comment_likes')
    liked = models.BooleanField(default=False)

    def __str__(self):
        if self.liked:
            return f"{self.user} liked {self.comment.content[:5]}"
        else:
            return f"{self.user} unliked {self.comment.content[:5]}"