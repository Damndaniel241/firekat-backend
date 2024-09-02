from rest_framework import serializers
from .models.topics import Topic
from .models.comments import Comment
from .models.subjects import Subject
from .models.faculties import Faculty
from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer

class TopicSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Topic
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'



class SubjectSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer(read_only=True)
    class Meta:
        model = Subject
        fields = '__all__'