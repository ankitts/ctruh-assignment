from rest_framework import serializers
from .models import Task 

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task_no', 'task_name', 'due_date', 'completed']
