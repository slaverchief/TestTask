
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from authsys.forms import SignUpForm, SignInForm
import secrets
from testTask.settings import HOST
from django.http import HttpResponseRedirect
class Main(ListView):
    model = TaskTracker
    context_object_name = 'tasktrackers'
    template_name = 'main/showtasktrackers.html'
    extra_context = {'title': 'Главная страница', 'form_login': SignInForm, 'form_signup': SignUpForm}

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return create_tasktracker(self.request)



class ShowTT(LoginRequiredMixin, DetailView):
    model = TaskTracker
    pk_url_kwarg = 'ttid'
    template_name = 'main/showtasktracker.html'
    context_object_name = 'tt'

    def post(self, request, *args, **kwargs):
        name = self.request.POST.get('name')
        if name:
            t = Task.objects.create(name=name, tt=TaskTracker.objects.get(pk=self.get_object().pk))
            TaskStatus.objects.create(task=t, status_code=1, executor=self.request.user)
        return HttpResponseRedirect(self.request.path_info)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['contributors'] = self.object.cotributions.all()
        context['title'] = self.object.name
        context['HOST'] = f'{HOST}'
        return context




@login_required
def create_tasktracker(request):
    tt = TaskTracker.objects.create(creator=request.user, name='Новый тасктрекер', join_slug=secrets.token_hex(5))
    tt.cotributions.add(request.user)
    return redirect("get_to_main")

@login_required
def join_contribution(request, join_slug):
    try:
        tt = TaskTracker.objects.get(join_slug=join_slug)
        if request.user not in tt.cotributions.all():
            tt.cotributions.add(request.user)
            tt.save()
    except ObjectDoesNotExist:
        pass
    return redirect('get_to_main')







