from django.contrib import admin

from core.api.v1.tasks.models.tasks import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'completed', 'created_at', 'updated_at')
