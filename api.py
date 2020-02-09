import requests
import json
from datetime import date
def post_resource():
	BASE_URL='http://127.0.0.1:8000/'
	ENDPOINT='api/'
	dat={
	"task_type":5,
	"task_desc":"task1"}
	json_data=json.dumps(dat)
	r=requests.post(BASE_URL+ENDPOINT,data=json_data)
	output=r.json()
	return output
post_resource()

def update_task(id):
	BASE_URL='http://127.0.0.1:8000/'
	ENDPOINT='api/'
	dat={
	'id':id,
	"task_type":1,
	"task_desc": "Updating the task descripton"}
	json_data=json.dumps(dat)
	r=requests.put(BASE_URL+ENDPOINT,data=json_data)
	output=r.json()
	return output
update_task(1)


def post_resource1():
	BASE_URL='http://127.0.0.1:8000/'
	ENDPOINT='api2/'
	print("idiot")
	dat={
	"task_type":1,
	"update_type":date(2019,8,4)}
	def default(obj):
		if isinstance(obj, date):
			return { '_isoformat': obj.isoformat() }
		return super().default(obj)
	json_data=json.dumps(dat,default=default)
	r=requests.post(BASE_URL+ENDPOINT,data=json_data)
	return r.json()


