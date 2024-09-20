from rest_framework import serializers

from core.api.v1.tasks.models.tasks import Task
from core.api.v1.tasks.exceptions.tasks import TaskTypeError


class TaskSerializer(serializers.Serializer):
    """Serializer for Task model."""
    
    class Meta:
        model = Task
        fields = ('__all__')

    def validate_title(self, title):
        if not isinstance(title, str) or len(title) < 1:
            raise TaskTypeError('Вы ввели не верный тип данных или длинна должна быть боль 1 символа!')
        return title
    
    def create(self, validated_data):
        return Task.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        return instance
