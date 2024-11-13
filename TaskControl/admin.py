from django.contrib import admin
from .models import *

admin.site.register(TaskTracker)
admin.site.register(Task)
admin.site.register(TaskStatus)