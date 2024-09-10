from rest_framework import serializers
from .models.topics import Topic
from .models.comments import Comment
from .models.subjects import Subject
from .models.faculties import Faculty
from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer




class CommentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
class TopicSerializer(serializers.ModelSerializer):
    # author = CustomUserSerializer(read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    comment_count = serializers.SerializerMethodField()
    comments = [CommentSerializer(read_only=True)]
    class Meta:
        model = Topic
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Replace the author ID with the full author object
        representation['author'] = CustomUserSerializer(instance.author).data
        return representation
    
    def get_comment_count(self, obj):
        return obj.posts.count()



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