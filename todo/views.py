from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework import views
from .models import Task
from .serializers import TaskSerializer, StatusSerializer
from messaging import tasks


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    model = Task

    @action(detail=True, methods=['POST'], name='execute')
    def execute(self, request, pk=None):
        """
        Не учитывается возможность отмены отметки выполнения задачи.
        """
        task = Task.objects.get(pk=pk)
        task.isDone = True
        task.save()
        tasks.send_message(pk)
        return Response(status=status.HTTP_200_OK)
