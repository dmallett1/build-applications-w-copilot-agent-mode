"""
URL configuration for octofit_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.urls import reverse
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, ActivityViewSet, LeaderboardViewSet, WorkoutViewSet

class CustomDefaultRouter(DefaultRouter):
    def get_api_root_view(self, *args, **kwargs):
        api_root_view = super().get_api_root_view(*args, **kwargs)
        api_root_view.cls.base_url = settings.ALLOWED_HOSTS[0]  # Use the first allowed host
        return api_root_view

router = CustomDefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activity', ActivityViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('api-root/', include(router.urls)),
]
