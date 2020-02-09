from django.shortcuts import render
import json
from django.http import HttpResponse
from .models import TaskTracker,Task
from .forms import TaskTrackerForm,TaskForm
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt,name='dispatch')
class apitask(View):
	def is_valid(self,data):
		try:
			emp=json.loads(data)
			valid=True
		except ValueError:
			valid=False
		return valid
	def get_task_by_objectid(self,id):
		try:
			task_object=Task.objects.get(id=id)
		except Task.DoesNotExist:
			task_object=None
		return task_object
	def post(self,request,*args,**kwargs):
		data=request.body
		task=json.loads(data)
		form=TaskForm(task)
		if form.is_valid():
			if 0<form.cleaned_data['task_type']>4:
			   json_data=json.dumps({"msg":"It is not a valid task,task-type should be 1,2,3,4"})
			else:
			    form.save(commit=True)
			    json_data=json.dumps({'msg':'data Inserted Successfully'})
			return HttpResponse(json_data)
	def put(self,request,*args,**kwargs):
		data=request.body
		den=json.loads(data)
		id=den.get('id',None)
		task_object=self.get_task_by_objectid(id)
		valid_json=self.is_valid(data)
		if not valid_json:
			json_data=json.dumps({'msg':'enter the valid data'})
			return HttpResponse(json_data)
		provided_data=json.loads(data)
		original_data={
		    "id":task_object.id,
		    "task_type":task_object.task_type,
		    "task_desc":task_object.task_desc
		}
		original_data.update(provided_data)
		form=TaskForm(original_data,instance=task_object)
		if form.is_valid():
			form.save(commit=True)
			json_data=json.dumps({'msg':'data Inserted Successfully'})
			return HttpResponse(json_data)
@method_decorator(csrf_exempt,name='dispatch')
class apitasktracker(View):
	def post(self,request,*args,**kwargs):
		data=request.body
		task=json.loads(data)
		form=TaskTrackerForm(task)
		if form.is_valid():
			form.save(commit=True)
			json_data=json.dumps({'msg':'data Inserted Successfully'})
			return HttpResponse(json_data)



# Create your views here.
