
"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app import views

router = DefaultRouter()
router.register('app', views.PDDLViewSet)
##router.register('upload',views.FileUploadView.as_view())
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    url(r'upload/(?P<filename>[^/]+)$',views.LinkUploadView.as_view()),
    path('help/', views.UserGuide.as_view()),
    url(r'downloadVisualisation', views.LinkDownloadPlanimation.as_view()),
    ]
