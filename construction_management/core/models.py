from django.contrib.auth.models import User
from django.db import models
 
class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
 
class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
 
class Project(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    timeline = models.DateField()
    created_by = models.ForeignKey(Manager, on_delete=models.CASCADE)
 
class Task(models.Model):
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    phase = models.CharField(max_length=100)