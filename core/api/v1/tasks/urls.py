from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.api.v1.tasks.handlers.tasks import TasksViewSet

app_name = 'task'
router_v1 = DefaultRouter()
router_v1.register(r'tasks', TasksViewSet, basename='tasks')

urlpatterns = [
    path('', include(router_v1.urls)),
]