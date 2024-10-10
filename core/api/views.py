from rest_framework.views import APIView
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models.topics import Topic
from .models.comments import Comment
from .models.subjects import Subject
from .models.faculties import Faculty
from .models.likes import Like
from .models.commentlikes import CommentLike
from .serializers import *
import json
import base64
from django.core.files.base import ContentFile
from django.db import IntegrityError

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all().order_by('-posted_at')
    serializer_class = TopicSerializer
    # permission_classes = [AllowAny]

    

    
    def get_permissions(self):
        if self.action in ['list','retrieve','comments','comment']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        topic = self.get_object()
        comments = topic.posts.all()  # related_name='subjects' used here
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    

    @action(detail=True, methods=['get'], url_path='comments/(?P<comment_pk>[^/.]+)')
    def comment(self, request, pk=None, comment_pk=None):
        topic = self.get_object()
        try:
            comment = topic.posts.get(pk=comment_pk)  # Assuming related_name='posts'
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        except Comment.DoesNotExist:
            return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
        
    
    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def get_like_status(self, request,pk=None, ):
        user= request.user
        topic= self.get_object()
        try:
            like_instance = Like.objects.get(user=user,topic=topic)
            return Response({'status':'success','like_status':like_instance.liked},status=status.HTTP_200_OK)
        except Like.DoesNotExist:
             return Response({
                'status': 'failure. No like exists',
                'like_status': False  # Assuming False when no Like instance is found
            }, status=status.HTTP_200_OK)

        
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        user = request.user
        topic = self.get_object()
        liked = request.data.get('liked')

        # Check if the Like already exists for this user and topic
        try:
            like_instance = Like.objects.get(user=user, topic=topic)
            # If it exists, update the 'liked' status
            like_instance.liked = liked
            like_instance.save()
            return Response({'message': 'Like updated successfully'}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            # If it doesn't exist, create a new like
            like_serializer = LikeSerializer(data=request.data)
            if like_serializer.is_valid():
                like_serializer.save(user=user, topic=topic)
                return Response(like_serializer.data, status=status.HTTP_201_CREATED)
            return Response(like_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def create(self, request, *args, **kwargs):
        print(request.FILES)
        topic_data = request.data
        topic_serializer = TopicSerializer(data=topic_data)

        if topic_serializer.is_valid():
            topic = topic_serializer.save()

            for file_key in ['image_1','image_2','image_3','image_4']:
                if file_key in request.FILES:
                    setattr(topic,file_key,request.FILES[file_key])

            topic.save()

           
            return Response(topic_serializer.data, status=status.HTTP_201_CREATED)
        return Response(topic_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = request.data.copy()
        
       

        try:
            removed_images = json.loads(data.get('removed_images', '[]'))
            if not isinstance(removed_images, list):
                removed_images = []
        except json.JSONDecodeError:
            removed_images = []

        print("Removing images:", removed_images)
        for image_field in removed_images:
            if hasattr(instance, image_field):
                image = getattr(instance, image_field)
                if image:
                    image.delete(save=False)
                    setattr(instance, image_field, None)

        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        for i in range(1, 5):
            file_key = f'image_{i}'
            existing_key = f'existing_image_{i}'
            if file_key in request.FILES:
                print(f"Updating {file_key}")
                setattr(instance, file_key, request.FILES[file_key])
            elif existing_key in data:
                print(f"Keeping existing {file_key}")
                # Do nothing, keep the existing image
            elif file_key not in removed_images:
                print(f"Clearing {file_key}")
                setattr(instance, file_key, None)


        instance.save()

        return Response(serializer.data)

# class LikeView(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self,request,id):
#         user = request.user
#         topic = Topic.objects.get(pk=id)
#         liked= request.data.get('liked')
        

#         # Check if the Like already exists for this user and topic
#         try:
#             like_instance = Like.objects.get(user=user,topic=topic)
#             # If it exists, update the 'liked' status
#             like_instance.liked = liked
#             like_instance.save()
#             return Response({'message':'Like updated successfully'},status=status.HTTP_200_OK)
#         except Like.DoesNotExist:
#             # If it doesn't exist, create a new like
#             like_serializer = LikeSerializer(data=request.data)
#             if like_serializer.is_valid():
#                 like_serializer.save(user=user,topic=topic)
#                 return Response(like_serializer.data, status=status.HTTP_201_CREATED)
#             return Response(like_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


            # like.save()
    
    
  

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        # Associate the authenticated user with the comment
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def get_comment_like_status(self, request,pk=None, ):
        user= request.user
        comment= self.get_object()
        try:
            like_instance = CommentLike.objects.get(user=user,comment=comment)
            return Response({'status':'success','comment_like_status':like_instance.liked},status=status.HTTP_200_OK)
        except CommentLike.DoesNotExist:
             return Response({
                'status': 'failure. No like exists',
                'Comment_like_status': False  # Assuming False when no Like instance is found
            }, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like_comment(self, request, pk=None):
        user = request.user
        comment = self.get_object()
        liked = request.data.get('liked')

        # Check if the Like already exists for this user and comment
        try:
            like_instance = CommentLike.objects.get(user=user, comment=comment)
            # If it exists, update the 'liked' status
            like_instance.liked = liked
            like_instance.save()
            return Response({'message': 'Comment Like updated successfully'}, status=status.HTTP_200_OK)
        except CommentLike.DoesNotExist:
            # If it doesn't exist, create a new like
            like_serializer = CommentLikeSerializer(data=request.data)
            if like_serializer.is_valid():
                like_serializer.save(user=user, comment=comment)
                return Response(like_serializer.data, status=status.HTTP_201_CREATED)
            return Response(like_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [AllowAny]
    # def get_permissions(self):
    #     if self.action in ['list','retrieve']:
    #         permission_classes = [AllowAny]
    #     else:
    #         permission_classes = [IsAuthenticated]
    #     return [permission() for permission in permission_classes]


    @action(detail=True, methods=['get'])
    def subjects(self, request, pk=None):
        faculty = self.get_object()
        subjects = faculty.subjects.all()  # related_name='subjects' used here
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)
    

    @action(detail=True, methods=['get'])
    def topics(self, request, pk=None):
        faculty = self.get_object()
        topics = faculty.topics.all()  # related_name='topics' is used here
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)
    
   

class CountTopicsView(APIView):
    # authentication_classes = []
    permission_classes = [AllowAny]

    def get(self,request):
        topic_count = Topic.objects.count()
        return Response(topic_count)


    
# from collections import deque

# def bfs(graph, start):
#     visited = set()
#     q = deque([start])
#     visited.add(start)


#     while q:
#         v= q.popleft()
#         print(v)

#         for u in graph[v]:
#             if u not in visited:
#                 visited.add(u)
#                 q.append(u)