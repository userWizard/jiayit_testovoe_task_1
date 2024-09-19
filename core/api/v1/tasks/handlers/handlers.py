from core.api.v1.tasks.shemas.serializers import TaskSerializer
from core.common.mixins import BaseCreateListRetriceUpdateDestroyApiVew


class TasksApiView(BaseCreateListRetriceUpdateDestroyApiVew):
    """Api View for CRUD list tasks"""
    serializer_class = TaskSerializer