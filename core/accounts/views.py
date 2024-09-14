from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import login,logout
from .models import CustomUser
from .serializers import RegisterSerializer,LoginSerializer,CustomUserSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token":token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)

            # user_serializer = CustomUserSerializer(user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
    

class getUserDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
    

class GetUserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)


class GetUserIdFromName(APIView):
    permission_classes = [AllowAny]

    def get(self,request,username):
        user = CustomUser.objects.filter(username=username).values('id').first()
        if user:
            user_id  = user['id']
        else:
            user_id = None
        
        return Response(str(user_id))


class CountUsersView(APIView):
    # authentication_classes = []
    permission_classes = [AllowAny]

    def get(self,request):
        user_count = CustomUser.objects.count()
        return Response(user_count)


















# class CustomUserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()

#     def get_serializer_class(self):
#         if self.action == 'create':
#             return RegisterSerializer
#         return CustomUserSerializer
    
#     def get_permissions(self):
#         if self.action == 'create':
#             return [permissions.AllowAny()]
#         elif self.action in ['update','partial_update','destroy']:
#             return [permissions.IsAuthenticated(),permissions.IsAdminUser()]
#         return [permissions.IsAuthenticated()]
    
#     @action(detail=False, methods=['get'])
#     def me(self, request):
#         serializer = CustomUserSerializer(request.user)
#         return Response(serializer.data)
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'user': CustomUserSerializer(user).data,
#             'token': token.key
#         }, status=status.HTTP_201_CREATED)