import json
import datetime


class Employee(object):
    employee ={}
    def __init__(self, emp_id, emp_name):
        self.employee["emp_name"] = emp_name
        self.employee["emp_id"] = emp_id
        self.employee["login_time"]=str(datetime.datetime.now())

    def add_task(self,task_title,task_description):
        self.task ={}
        self.task["task_title"]=task_title
        self.task["task_description"]=task_description
        self.task["start_time"] = str(datetime.datetime.now())

    def task_end(self, task_success):
        self.task["end_time"] = str(datetime.datetime.now())
        self.task["task_success"] = task_success


    def logout(self):
        self.employee["logout_time"] = str(datetime.datetime.now())
        filename = f"{self.employee['emp_name']}_{str(datetime.datetime.now().date())}.json"
        with open(filename,"w")as f:
            f.write(json.dumps(self.employee))
emp = Employee(1,"ammu")
emp.add_task("op","csv")
emp.task_end("g")
emp.logout()

