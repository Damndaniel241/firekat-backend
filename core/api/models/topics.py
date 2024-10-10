from django.db import models
from .subjects import Subject
from accounts.models import CustomUser
from .faculties import Faculty
from django.utils import  timezone

from autoslug import AutoSlugField


class Topic(models.Model):
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='title',null=False, unique=True,default=None)
    content = models.TextField(blank=True)
    posted_at = models.DateTimeField(default=timezone.now)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,blank=True,null=True, related_name='topics')
    author = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True, related_name="owned_topics")
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True, related_name="topics")
    image_1 = models.ImageField(upload_to='post_images/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='post_images/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='post_images/', null=True, blank=True)
    image_4 = models.ImageField(upload_to='post_images/', null=True, blank=True)
    


    def clean(self):
        from django.core.exceptions import ValidationError
        if not self.subject and not self.faculty:
            raise ValidationError('A topic must be associated with either a Subject or a Faculty.')
        
    def delete_image(self, image_field):
        image = getattr(self, image_field)
        if image:
            image.delete(save=False)
            setattr(self, image_field, None)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)



    def __str__(self):
        return f"{self.title} - {self.subject if self.subject else self.faculty}"

# class TopicImage(models.Model):
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='topic_images')
#     image = models.ImageField(upload_to='post_images/', null=True, blank=True)