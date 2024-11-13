from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models import SET_NULL
from django.db.models.functions import Now


class TaskTracker(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(User, related_name='task_trackers', on_delete=models.CASCADE)
    cotributions = models.ManyToManyField(User)
    join_slug = models.SlugField(max_length=10)

    def __str__(self):
        return self.name

class TaskStatus(models.Model):
    status_code = models.PositiveSmallIntegerField(validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ])
    executor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, editable=False)
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='task_statuses')

    def get_string_status(self):
        if self.status_code == 1:
            return "Задача создана"
        elif self.status_code == 2:
            return "Назначен исполнитель"
        elif self.status_code == 3:
            return "Задача выполнена"
        else:
            return "Задача проверена"

    def __str__(self):
        return f'Task {self.task.name} with status {self.get_string_status()}'

    class Meta:
        unique_together = ('status_code', 'task')

DEFAULT_DESC = 'Здесь должно было быть описание задачи'

class Task(models.Model):
    name = models.CharField(max_length=255)
    executor = models.ForeignKey(User, on_delete=SET_NULL, null=True, blank=True)
    tt = models.ForeignKey(TaskTracker, on_delete=models.CASCADE, related_name='tasks')
    desc = models.TextField(default=DEFAULT_DESC)

    def has_executor(self):
        try:
            TaskStatus.objects.get(status_code=2, task__pk=self.pk)
            return True
        except ObjectDoesNotExist:
            return False

    def is_executed(self):
        try:
            TaskStatus.objects.get(status_code=3, task__pk=self.pk)
            return True
        except ObjectDoesNotExist:
            return False

    def is_checked(self):
        try:
            t = TaskStatus.objects.get(status_code=4, task__pk=self.pk)
            return True
        except ObjectDoesNotExist:
            return False

    def __str__(self):
        return self.name


# Create your models here.