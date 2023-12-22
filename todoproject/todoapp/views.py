from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib.auth.views import LoginView

from todoapp.models import Task


# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = "tasks"


class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"


class TaskCreate(CreateView):
    model = Task
    # fields = ['title', 'description', ...]と同じ
    fields = "__all__"
    # リダイレクト
    success_url = reverse_lazy("tasks")


class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class TaskDelete(DeleteView):
    model = Task
    context_object_name = "task"
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class TaskListLoginView(LoginView):
    # ここのallはUserモデルのall
    fields = "__all__"
    # template_nameを書き換えない場合、registration/login.htmlに定義する
    template_name = "todoapp/login.html"

    def get_success_url(self):
        return reverse_lazy("tasks")
