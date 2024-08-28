from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models.topics import Topic

@receiver(pre_save, sender=Topic)
def create_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

    # Ensure uniqueness of slug
    original_slug = instance.slug
    counter = 1
    while Topic.objects.filter(slug=instance.slug).exists():
        instance.slug = f"{original_slug}-{counter}"
        counter += 1