"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import ObtainAuthToken
from django.conf import settings
from django.conf.urls.static import static
from accounts.api import router as accounts_router
from ninja import NinjaAPI
from rest_framework.schemas import get_schema_view
from rest_framework.renderers import JSONOpenAPIRenderer

schema_view = get_schema_view(
    title="accounts",
    renderer_classes=[JSONOpenAPIRenderer],
)

# api = NinjaAPI()
# api.add_router("api/", accounts_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('api/token/', ObtainAuthToken.as_view()),
    path('api/',include('api.urls')),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT)