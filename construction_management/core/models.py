from django.db import models
from django.contrib.auth.models import User
 
 
# Supervisor Model
class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # Add name field
    email = models.EmailField(max_length=254)  # Add email field
    mobile_number = models.CharField(max_length=15)  # Add mobile number field
 
    def __str__(self):
        return self.name  # You can also return user.username if preferred

# Manager Model
class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # Add name field
    email = models.EmailField(default='default@example.com') 
    mobile_number = models.CharField(max_length=15)  # Add mobile number field
 
    def __str__(self):
        return self.name  # You can also return user.username if preferred
 
# Project Model
class Project(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    timeline = models.DateField()
    created_by = models.ForeignKey(Manager, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null=True, blank=True)
 
    def __str__(self):
        return self.name
 
# Worker Model
class Worker(models.Model):
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=100)
 
    def __str__(self):
        return self.name
 
# Task Model
class Task(models.Model):
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    workers = models.ManyToManyField(User)  # Assuming workers are also users
    task_picture = models.ImageField(upload_to='tasks/')  # Adjust path as needed
    estimated_time = models.IntegerField(null=True, blank=True)  # Stores estimated time to complete the task
    description = models.TextField()
    deadline = models.DateField()
    phase = models.CharField(max_length=100)
 
    def __str__(self):
        return self.title