import json
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from TaskControl.models import *


@csrf_exempt
@login_required()
def rename(request, ttid):
    if request.method == "POST":
        tt = TaskTracker.objects.get(pk=ttid)
        if tt.creator != request.user:
            return HttpResponse(status=403)
        data = json.loads(request.body)
        name = data.get('name')
        if not name:
            return HttpResponse(status = 400)
        tt.name = name
        tt.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status = 400)

@csrf_exempt
@login_required()
def assign_executor(request):
    if request.method == "POST":
        data = json.loads(request.body)
        tid = data.get('task_id')
        cid = data.get('user_id')
        executor = User.objects.get(pk=cid)
        t = Task.objects.get(pk=tid)
        ts = None
        if not t.has_executor():
            ts = TaskStatus.objects.create(status_code=2, task=t, executor=request.user)
        else:
            if t.is_executed():
                TaskStatus.objects.get(status_code=3, task=t).delete()
            if t.is_checked():
                TaskStatus.objects.get(status_code=4, task=t).delete()
        t.executor = executor
        t.save()
        t.task_statuses.add(ts)
        return HttpResponse(status = 200)
    else:
        return HttpResponse(status=400)

@csrf_exempt
@login_required()
def delete_task(request):
    if request.method == "POST":
        data = json.loads(request.body)
        tid = data.get('task_id')
        t = Task.objects.get(pk=tid)
        t.delete()
        return HttpResponse(status = 200)
    else:
        return HttpResponse(status=400)

@csrf_exempt
@login_required()
def execute_task(request):
    if request.method == "POST":
        data = json.loads(request.body)
        tid = data.get('task_id')
        t = Task.objects.get(pk=tid)
        if not t.is_executed():
            TaskStatus.objects.create(status_code=3, task=t, executor=request.user)
        return HttpResponse(status = 200)
    else:
        return HttpResponse(status=400)

@csrf_exempt
@login_required()
def check_task(request):
    if request.method == "POST":
        data = json.loads(request.body)
        tid = data.get('task_id')
        t = Task.objects.get(pk=tid)
        if not t.is_checked():
            TaskStatus.objects.create(status_code=4, task=t, executor=request.user)
        return HttpResponse(status = 200)
    else:
        return HttpResponse(status=400)

@csrf_exempt
@login_required()
def edit_desc_text(request):
    if request.method == "POST":
        data = json.loads(request.body)
        tid = data.get('task_id')
        text = data.get('text')
        t = Task.objects.get(pk=tid)
        t.desc = text
        t.save()
        return HttpResponse(status = 200)
    else:
        return HttpResponse(status=400)