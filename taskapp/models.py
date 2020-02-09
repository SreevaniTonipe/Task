from django.db import models
from datetime import timedelta
# Create your models here.
class Task(models.Model):
	task_type=models.IntegerField()
	task_desc=models.CharField(max_length=30)
	def func(task_desc):
		if len(task_desc)>30:
			print("bnvfgb")
class TaskTracker(models.Model):
	task_type=models.IntegerField()
	update_type=models.DateField(timedelta(weeks=1))
