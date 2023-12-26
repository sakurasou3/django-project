from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from todoapp.models import Task


# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # fields = ['title', 'description', ...]と同じ
    # fields = "__all__"
    # Userを入力しないようにする
    fields = ["title", "description", "completed"]
    # リダイレクト
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class TaskDelete(LoginRequiredMixin, DeleteView):
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


class RegisterTodoApp(FormView):
    template_name = "todoapp/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        # form情報を一時保存しておく
        user = form.save()
        if user is not None:
            # userが作成されれば、ログインを行う
            login(self.request, user)
        return super().form_valid(form)
