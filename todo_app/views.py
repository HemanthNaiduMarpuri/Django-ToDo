from sqlite3 import Date
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View, generic
from .models import User, Task
from .forms import SignUpForm, LoginForm, TaskCreateForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from .mixins import LoginRequiredMixin


class SignUpView(generic.CreateView):
    model = User
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)
    

class LoginView(generic.FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)    
        return super().form_valid(form)
    
class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'taskcreate.html'
    form_class = TaskCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = 'todos'
    template_name = 'home.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user, trashed=False).order_by('-created_at')

class TaskTrashView(LoginRequiredMixin, View):
    template_name = 'tasktrash.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def get(self, request, pk):
        task = get_object_or_404(self.get_queryset(), pk=pk)
        return render(request ,self.template_name, {'task':task})
    
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'], user=request.user)
        task.trashed = True
        task.trashed_at = Date.today()
        task.save()
        return redirect(self.success_url)
    
class TrashedListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'trashedtasklist.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user ,trashed=True).order_by('-created_at')
    
class DeleteTaskPermanentlyView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = 'taskdelete.html'
    success_url = reverse_lazy('deleted-task-list')
    context_object_name = 'task'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
class RestoreTaskView(LoginRequiredMixin, View):
    template_name = 'restoretask.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def get(self, request, pk):
        task = get_object_or_404(self.get_queryset(), pk=pk)
        return render(request, self.template_name, {'task': task})
    
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'], user=request.user)
        task.trashed = False
        task.save()
        return redirect(self.success_url)  

class CompletedTaskView(LoginRequiredMixin, View):
    template_name = 'completetask.html'
    success_url = reverse_lazy('completed-task-list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def get(self, request, pk):
        task = get_object_or_404(self.get_queryset(), pk=pk)
        return render(request, self.template_name, {'task':task})
    
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'], user=request.user)
        task.completed = True
        task.completed_at = Date.today()
        task.save()
        return redirect(self.success_url)
    
class CompletedTaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'completedtasklist.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user, completed=True).order_by('-created_at')
    
class ImportantTaskView(LoginRequiredMixin, View):
    template_name = 'importanttask.html'
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def get(self, request, pk):
        task = get_object_or_404(self.get_queryset(), pk=pk)
        return render(request, self.template_name, {'task':task})
    
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'], user=request.user)
        task.important = True
        task.save()
        return redirect(self.success_url)

class ImportantTaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = 'importanttasklist.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user, important=True).order_by('-created_at')