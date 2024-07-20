from django.urls import path,include
from . import views
urlpatterns = [
    path("Project/Project_list",views.ProjectListView.as_view(),name="Project_list"), # type: ignore
    path("Project/Create",views.ProjectCreatView.as_view(),name="Project_create"), # type: ignore
    path("Project/edit/<int:pk>",views.ProjectUpdateView.as_view(),name="Project_update"), # type: ignore
    path("Project/delete/<int:pk>", views.ProjectDeleteView.as_view(), name="Project_delete"),
    path("Task/Create",views.TaskCreateView.as_view(),name="Task_Create"), # type: ignore
    path("Task/Update/<int:pk>",views.TaskUpdateView.as_view(),name="Task_update"),
    path("Task/Delete/<int:pk>",views.TaskDeleteView.as_view(),name="Task_delete"), # type: ignore

]
