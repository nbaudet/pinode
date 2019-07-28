"""pinode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
import homepage
from homepage import views
from rest_service.views import UserViewSet, GroupViewSet, NodeViewSet, ActivityViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'nodes', NodeViewSet)
router.register(r'activities', ActivityViewSet)

urlpatterns = [
    # Homepage
    path("", homepage.views.Home.as_view()),
    # Browsable API
    path('', include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # Admin
    path("admin/", admin.site.urls),
]

# Debug toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

