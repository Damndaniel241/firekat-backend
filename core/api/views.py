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
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

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
    
   