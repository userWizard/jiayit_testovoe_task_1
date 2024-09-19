from django.db import models

from core.common.models import TimedBaseModel

class Task(TimedBaseModel):
    """Model list of tasks"""
    title = models.CharField(
        verbose_name='Название',
        max_length=100,
    )
    description = models.TextField(
        verbose_name='Описание',
        max_length=100,
        blank=True,
    )
    completed = models.BooleanField(
        verbose_name='Выполнена задача или нет',
        default=False,
    )
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'