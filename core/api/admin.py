from django.contrib import admin

# Register your models here.
from .models.faculties import Faculty
from .models.subjects import Subject
from .models.comments import Comment
from .models.topics import Topic
from .models.likes import Like
from .models.commentlikes import CommentLike



# class TopicAdmin(admin.ModelAdmin):
#   list_display = ("title")
#   prepopulated_fields = {"slug": ("title")}


admin.site.register(Faculty)
admin.site.register(Subject)
admin.site.register(Comment)
admin.site.register(Topic)
admin.site.register(Like)
admin.site.register(CommentLike)


  
