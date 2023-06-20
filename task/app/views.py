from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

def index(request):
    return HttpResponse("Hello! You are at index.")

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # to show all tasks ordered by due date
    def list(self, request):
        queryset = Task.objects.all().order_by('due_date')
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
    
    # to show incomplete tasks
    def list_remaining(self, request):                              
        queryset = Task.objects.all().filter(completed=False).order_by('due_date')             
        serializer = TaskSerializer(queryset, many=True)
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

        # queryset = Task.objects.all()
        # task = get_object_or_404(queryset, task_no=pk)
        # serializer = TaskSerializer(task)
        # return Response(serializer.data)
    
    # to create a task with task_no, task_name, due_date as necessary fields 
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
        # task_no = request.data['task_no']
        # task_name = request.data['task_name']
        # due_date = request.data['due_date']
        # completed = 0
        # if('completed' in request.data):
        #     completed = request.data['completed'] 
        # if(Task.objects.check(task_no = task_no)):
        #     return Response("Task number is already taken!")    
        # task = Task(task_no = task_no, due_date = due_date, task_name = task_name, completed= completed)      
        # serializer = TaskSerializer(task)
        # serializer.is_valid(raise_exception=True)
        # task.save()
        # return Response(serializer.data)
    
    # to update a task with task_no=pk
    def partial_update(self, request, pk=None):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, task_no=pk)
        if('task_name' in request.data): 
            task_name = request.data['task_name']
            task.task_name = task_name
        if('completed' in request.data):
            completed = request.data['completed']
            task.completed = completed
        if('due_date' in request.data):
            due_date = request.data['due_date']
            task.due_date = due_date  
        serializer = TaskSerializer(task)
        serializer.is_valid(raise_exception=True)
        task.save()
        return Response(serializer.data)
    
    # to delete a task with task_no = pk
    def destroy(self, request, pk=None):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, task_no=pk)
        task.delete()
        return Response("Task %s deleted" %pk)
    
