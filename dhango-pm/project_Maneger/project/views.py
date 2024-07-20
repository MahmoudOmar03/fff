from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from . import models,forms
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.


class ProjectListView(LoginRequiredMixin,ListView):
    model=models.Project
    template_name="project/list.html"
    paginate_by=6 #limt how card can apper
    def get_queryset(self):
        queryset= super().get_queryset()
        where={'user_id':self.request.user}
        q=self.request.GET.get("q",None)
        if q:
            where['title__icontains']=q
        return queryset.filter(**where)


class ProjectCreatView(LoginRequiredMixin,CreateView):
    model=models.Project
    form_class=forms.projectCreatForm
    template_name="project/creat.html"
    def get_success_url(self):
        return "Project_list"
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=models.Project
    form_class=forms.projectUpdateForm
    template_name="project/update.html"
    def test_func(self):
        return self.get_object().user_id==self.request.user.id



    def get_success_url(self):
        return reverse("Project_update", args=[self.object.id]) # type: ignore

from django.urls import reverse_lazy

class ProjectDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = models.Project
    template_name = "project/delete.html"
    success_url = reverse_lazy('Project_list')
    def test_func(self):
        return models.Project.objects.get(pk=project_id).user_id == self.request.user.id

    
class TaskCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model=models.Task
    fields=["project","descreption"]
    template_name='project/update.html'
    http_method_name=["post"]#to make the path to create

    def test_func(self):
        project_id=self.request.POST.get('project','')
        return self.get_object().user_id==self.request.user.id

    
    def get_success_url(self):
        return reverse("Project_update", args=[self.object.project.id])    
    
class TaskUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=models.Task
    fields=["is_completed"]
    http_method_name=["post"]#to make the path to just create

    def test_func(self):
        return self.get_object().project.user_id==self.request.user.id

    def get_success_url(self):
        return reverse("Project_update", args=[self.object.project.id])    
    
class TaskDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=models.Task

    def test_func(self):
        return self.get_object().project.user_id==self.request.user.id

    def get_success_url(self):
        return reverse("Project_update", args=[self.object.project.id])   