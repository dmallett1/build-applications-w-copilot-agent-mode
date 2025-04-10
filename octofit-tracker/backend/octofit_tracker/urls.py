"""
URL configuration for octofit_tracker project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.urls import reverse
from rest_framework.routers import DefaultRouter
from rest_framework.views import APIView
from rest_framework.response import Response
from .views import UserViewSet, TeamViewSet, ActivitiesViewSet, LeaderboardViewSet, WorkoutViewSet

class CustomAPIRootView(APIView):
    api_root_dict = None  # Add this attribute to handle the argument

    def get(self, request, *args, **kwargs):
        base_url = "https://friendly-xylophone-x54vg49qwgx3p4xg-8000.app.github.dev"
        return Response({
            "users": f"{base_url}/api-root/users/",
            "teams": f"{base_url}/api-root/teams/",
            "activities": f"{base_url}/api-root/activities/",
            "leaderboard": f"{base_url}/api-root/leaderboard/",
            "workouts": f"{base_url}/api-root/workouts/",
        })

class CustomDefaultRouter(DefaultRouter):
    api_root_dict = None  # Add this attribute to handle the argument

    def get_api_root_view(self, *args, **kwargs):
        api_root_view = super().get_api_root_view(*args, **kwargs)
        api_root_view.cls.base_url = settings.ALLOWED_HOSTS[0]  # Use the first allowed host
        return api_root_view

router = CustomDefaultRouter()
router.APIRootView = CustomAPIRootView
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivitiesViewSet)
router.register(r'leaderboard', LeaderboardViewSet)
router.register(r'workouts', WorkoutViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('api-root/', include(router.urls)),
]
