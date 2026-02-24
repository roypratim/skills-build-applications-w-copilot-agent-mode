
# octofit_tracker URL Configuration
# REST API endpoint format: https://$CODESPACE_NAME-8000.app.github.dev/api/[component]/
# Example: https://$CODESPACE_NAME-8000.app.github.dev/api/activities/
# Uses the CODESPACE_NAME environment variable for codespace URL.

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'teams', views.TeamViewSet, basename='team')
router.register(r'activities', views.ActivityViewSet, basename='activity')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')
router.register(r'leaderboard', views.LeaderboardViewSet, basename='leaderboard')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.api_root, name='api-root'),
    path('api/', include(router.urls)),
]
