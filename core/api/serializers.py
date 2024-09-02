from rest_framework import serializers
from .models.topics import Topic
from .models.comments import Comment
from .models.subjects import Subject
from .models.faculties import Faculty
from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer


class TopicSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    comment_count = serializers.SerializerMethodField()
    class Meta:
        model = Topic
        fields = '__all__'

    def get_comment_count(self, obj):
        return obj.posts.count()
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class FacultySerializer(serializers.ModelSerializer):
    # user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Faculty
        fields = '__all__'



class SubjectSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer(read_only=True)
    class Meta:
        model = Subject
        fields = '__all__'