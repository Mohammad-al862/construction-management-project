from django.urls import path
from .views import (
    register_user, login_user, logout_user, my_profile,
    create_project, list_projects, retrieve_project,
    create_task, list_tasks
)
 
urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('my-profile/', my_profile, name='my-profile'),
    path('projects/', list_projects, name='list-projects'),
    path('projects/<int:project_id>/', retrieve_project, name='retrieve-project'),
    path('projects/create/', create_project, name='create-project'),
    path('projects/<int:project_id>/tasks/', list_tasks, name='list-tasks'),
    path('tasks/create/', create_task, name='create-task'),
]