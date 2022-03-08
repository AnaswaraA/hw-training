import json
from datetime import datetime

t = []

class Employes:
    def __init__(self, emp_id, emp_name):
        self.emp_name = emp_name
        self.emp_id = emp_id

    def login(self):
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M")

    def task_start(self, task_title, task_description):
        return task_title, task_description

    def task_start_time(self):
        n= datetime.now()
        return n.strftime("%Y-%m-%d %H:%M")

    def task_end_time(self):
        o= datetime.now()
        return o.strftime("%Y-%m-%d %H:%M")

    def task_end(self, success):
        return success

    def logout(self):
        w = datetime.now()
        return w.strftime("%Y-%m-%d %H:%M")
emp = Employes(1,"Ammu")
task_title1, task_description1 = emp.task_start('first','task ')
task_title2 , task_description2 = emp.task_start('second','day')
task_title3 , task_description3 = emp.task_start('third','titles are starting with capital letters')
success1 = emp.task_end('True')
success2 = emp.task_end('false')
success3 = emp.task_end('True')
task1 ={
'task_title':task_title1,
    'task_description':task_description1,
    'start_time':emp.task_start_time(),
    'end_time':emp.task_end_time(),
    'task_sucess':success1
}
task2 ={
'task_title':task_title2,
    'task_description':task_description2,
    'start_time':emp.task_start_time(),
    'end_time':emp.task_end_time(),
    'task_sucess':success2
}
task2 ={
'task_title':task_title2,
    'task_description':task_description2,
    'start_time':emp.task_start_time(),
    'end_time':emp.task_end_time(),
    'task_sucess':success2
}
task3 ={
'task_title':task_title3,
    'task_description':task_description3,
    'start_time':emp.task_start_time(),
    'end_time':emp.task_end_time(),
    'task_sucess':success3
}

t.append(task1)
t.append(task2)
t.append(task3)
details = {
    'name': emp.emp_name,
    'emp_id':emp.emp_id,
    'login_time': emp.login(),
    'logout_time':emp.logout(),
    'task': t
}
print(details)
n= datetime.now().strftime("%Y-%m-%d ")
with open("2022-03-08Ammu.json", "w") as fp:
    json.dump(details, fp)

