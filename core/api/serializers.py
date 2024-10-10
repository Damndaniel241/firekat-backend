from rest_framework import serializers
from .models.topics import Topic
from .models.comments import Comment
from .models.subjects import Subject
from .models.faculties import Faculty
from accounts.models import CustomUser
from .models.likes import Like
from accounts.serializers import CustomUserSerializer


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'
    # user 


class CommentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    # quoted_comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all)


    class Meta:
        model = Comment
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.quoted_comment:
            # Use CommentSerializer to represent the quoted comment instead of just the ID
            representation['quoted_comment'] = CommentSerializer(instance.quoted_comment).data
        else:
            representation['quoted_comment'] = None

        return representation



class TopicSerializer(serializers.ModelSerializer):
    # author = CustomUserSerializer(read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
   

    comments = [CommentSerializer(read_only=True)]
   
    class Meta:
        model = Topic
        fields = '__all__'


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Replace the author ID with the full author object
        representation['author'] = CustomUserSerializer(instance.author).data

        request = self.context.get('request')
    
    # Only include 'like_status' if the user is authenticated
        if request and not request.user.is_authenticated:
            representation.pop('like_status', None)
        return representation
    
    def get_comment_count(self, obj):
        return obj.posts.count()

    def get_like_count(self, obj):
        queryset = obj.likes.filter(liked=True)
        user_liked_list_count = len(list(queryset))
        return user_liked_list_count
    





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