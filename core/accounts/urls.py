from django.urls import path,include
from .views import RegisterView, LoginView, LogoutView,UserViewSet,GetUserDetailsView
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    # path('user/<id>', getUserDetail.as_view()),
    path('', include(router.urls)),
    path('users/me/', GetUserDetailsView.as_view()),
]
