from rest_framework import serializers
from .models.topics import Topic,TopicImage
from .models.comments import Comment
from .models.subjects import Subject
from .models.faculties import Faculty
from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer




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

class TopicImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicImage
        fields = ('image',)

class TopicSerializer(serializers.ModelSerializer):
    # author = CustomUserSerializer(read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    comment_count = serializers.SerializerMethodField()
    comments = [CommentSerializer(read_only=True)]
    # topic_images = TopicImageSerializer(many=True, read_only=True)
    # images = serializers.ListField(
    #     child=serializers.ImageField(max_length=100000, allow_empty_file=False, use_url=False),
    #     write_only=True,
    #     required=False
    # )

    class Meta:
        model = Topic
        fields = '__all__'
    # class Meta:
    #     model = Topic
    #     fields = ['title', 'content', 'posted_at', 'author', 'faculty', 'subject', 'topic_images', 'images','comment_count']

    # def create(self, validated_data):
    #     images_data = validated_data.pop('images', [])
    #     topic = Topic.objects.create(**validated_data)

    #     # Create TopicImage instances for each uploaded image
    #     for image_data in images_data:
    #         TopicImage.objects.create(topic=topic, image=image_data)

    #     return topic

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