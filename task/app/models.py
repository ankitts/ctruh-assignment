from django.db import models

# Create your models here.

class Task(models.Model):
    task_no = models.IntegerField(primary_key=True)
    task_name = models.CharField(max_length=200)
    due_date = models.DateField(null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name
