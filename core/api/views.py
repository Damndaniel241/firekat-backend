from rest_framework.views import APIView
from rest_framework import viewsets
from .models.topics import Topic
from .serializers import TopicSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer