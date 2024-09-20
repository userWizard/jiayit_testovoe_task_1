from rest_framework import viewsets

from core.api.v1.tasks.models.tasks import Task
from core.api.v1.tasks.shemas.serializers import TaskSerializer

class TasksViewSet(viewsets.ModelViewSet):
    """ViewSet for CRUD list tasks"""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
