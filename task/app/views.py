from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Task
from .serializers import TaskSerializer

def index(request):
    return HttpResponse("Hello! You are at index.")

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    # to show all tasks ordered by due date
    def list(self, request):
        tasks = Task.objects.all().order_by('due_date')
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)
    
    # to show incomplete tasks
    def list_remaining(self, request):                              
        tasks = Task.objects.all().filter(completed=False).order_by('due_date')             
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

    # to show a task using its task_no
    def retrieve(self, request, pk=None):
        try:
            task = self.get_object()
            serializer = self.get_serializer(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response(
                {'error': 'Task not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    # to create a task with task_no, task_name, due_date as necessary fields 
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
    
    # to update a task with task_no=pk
    def partial_update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    # to delete a task with task_no = pk
    def destroy(self, request, pk=None):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        try:
            task = self.get_object()
            task.completed = True
            task.save()
            serializer = self.get_serializer(task)
            return Response(serializer.data)
        except Task.DoesNotExist:
            return Response(
                {'error': 'Task not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
    
