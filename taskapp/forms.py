from django import forms
from .models import TaskTracker,Task
class TaskTrackerForm(forms.ModelForm):
	class Meta:
		model=TaskTracker
		fields='__all__'

class TaskForm(forms.ModelForm):
	class Meta:
		model=Task
		fields="__all__"