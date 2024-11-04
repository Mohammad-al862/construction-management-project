from django.contrib import admin
from .models import Project, Task, Manager, Supervisor

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'budget', 'timeline', 'supervisor')  # Ensure supervisor field is valid
    search_fields = ('name', 'location')
    list_filter = ('timeline', 'supervisor')  # Supervisor should be a valid ForeignKey

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'deadline')  # Changed 'due_date' to 'deadline' to match model
    search_fields = ('name', 'project__name')
    list_filter = ('deadline',)  # Changed 'due_date' to 'deadline'

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username', 'user__email')

class SupervisorAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username', 'user__email')

# Registering models with the admin site
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Supervisor, SupervisorAdmin)
