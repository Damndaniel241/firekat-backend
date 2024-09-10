from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models.topics import Topic
from .models.comments import Comment
from .models.subjects import Subject
from .models.faculties import Faculty
from .serializers import *

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all().order_by('-posted_at')
    serializer_class = TopicSerializer
    permission_classes = [AllowAny]


    # def get_permissions(self):
    #     if self.action in ['list','retrieve']:
    #         permission_classes = [AllowAny]
    #     else:
    #         permission_classes = [IsAuthenticated]
    #     return [permission() for permission in permission_classes]
    
    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        topic = self.get_object()
        comments = topic.posts.all()  # related_name='subjects' used here
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

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