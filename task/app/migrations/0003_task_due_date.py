# Generated by Django 4.2.2 on 2023-06-20 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_remove_task_id_alter_task_task_no"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="due_date",
            field=models.DateField(null=True),
        ),
    ]
