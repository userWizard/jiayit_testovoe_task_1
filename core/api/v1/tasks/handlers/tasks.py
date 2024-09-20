# from django.shortcuts import get_object_or_404
from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework import status

from core.api.v1.tasks.models.tasks import Task
from core.api.v1.tasks.shemas.serializers import TaskSerializer

class TasksViewSet(viewsets.ModelViewSet):
    """ViewSet for CRUD list tasks"""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
