from rest_framework import serializers

from core.api.v1.tasks.models.tasks import Task

class TaskSerializer(serializers.Serializer):
    """Serializer for Task model."""
    
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'completed')