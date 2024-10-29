from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Manager, Supervisor, Project, Task
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
 
class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['user']
 
class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = ['user']
 
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'location', 'budget', 'timeline', 'supervisor']
 
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'project', 'name', 'workers', 'task_picture', 'estimated_time', 'description', 'deadline']