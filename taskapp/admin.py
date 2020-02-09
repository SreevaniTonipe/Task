from django.contrib import admin
from taskapp.models import Task,TaskTracker


class TaskAdmin(admin.ModelAdmin):
	list_display=['task_type','task_desc']

class TaskTrackerAdmin(admin.ModelAdmin):
	list_display=['task_type',"update_type"]

admin.site.register(Task,TaskAdmin)
admin.site.register(TaskTracker,TaskTrackerAdmin)
# Register your models here.
