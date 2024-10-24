from rest_framework import serializers
from django.contrib.auth.models import User
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
        fields = ['id', 'name', 'location', 'budget', 'timeline', 'created_by']
 
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'project', 'name', 'description', 'deadline', 'phase']