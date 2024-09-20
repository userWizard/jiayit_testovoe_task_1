# tasks/tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from core.api.v1.tasks.models.tasks import Task
from core.api.v1.tasks.shemas.serializers import TaskSerializer

client = APIClient()

class TaskAPITestCase(TestCase):
    """ Test module for Task API """

    def setUp(self):
        Task.objects.create(title='Task 1', description='Description 1')
        Task.objects.create(title='Task 2', description='Description 2')

    def test_get_all_tasks(self):
        response = client.get('/api/tasks/')
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        data = {'title': 'New Task', 'description': 'New Description'}
        response = client.post('/api/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_task(self):
        task = Task.objects.get(title='Task 1')
        data = {'title': 'Updated Task', 'description': 'Updated Description'}
        response = client.put(f'/api/tasks/{task.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        task = Task.objects.get(title='Task 1')
        response = client.delete(f'/api/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
