import json
from flask import Flask, render_template,request
import subprocess
import os
from datetime import datetime
import RPi.GPIO as GPIO
app = Flask(__name__)
data = []
def get_rfid_data(filename='rfid_data.json'):
try:
with open(filename, 'r') as file:
data = json.load(file)
# Convert dictionary values to a list
if isinstance(data, dict):
data = list(data.values())
else:
data = []
except FileNotFoundError:
data = []
except json.JSONDecodeError:
data = []
return data
@app.route('/activitylog/')
def rfid_data():
data = get_rfid_data()
return render_template('log.html', data=data)
@app.route('/taskinput/',methods=['GET', 'POST'])
def task_input():
data = []
if request.method == 'POST':
if os.path.exists('input_task.json'):
with open('input_task.json','r') as file:
data = json.load(file)
user_input = request.form['user_input']
user_date = request.form['date']
user_time = request.form['time']
data1 = {'task' : user_input,
'date' : user_date,
'time' : user_time}
data.append(data1)
with open('input_task.json','w') as file:
json.dump(data,file)
return render_template('input.html')
@app.route('/tasks/',methods=['GET', 'POST'])
def disp_tasks(filename = 'input_task.json'):
try:
with open(filename,'r') as file:
tasks = json.load(file)
if os.path.exists('rfid_data.json'):
with open('rfid_data.json','r') as file:
if file.read().strip() != "":
file.seek(0)
data = json.load(file)
comp_tasks = list(data.values())
else:
comp_tasks=[]
else:
comp_tasks=[]
print(tasks)
n = 0
now = datetime.now()
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
cur_year = int(formatted_now[0:4])
cur_month = int(formatted_now[5:7])
cur_day = int(formatted_now[8:10])
cur_hour = int(formatted_now[11:13])
cur_minute = int(formatted_now[14:16])
for i in tasks:
input_task = i['task'].strip().lower()
date_year = int(i['date'][0:4])
date_month =int(i['date'][5:7])
date_day = int(i['date'][8:10])
time_hour =int(i['time'][0:2])
time_minute = int(i['time'][3:5])
for j in comp_tasks:
task= j['data'].strip().lower()
comp_year = int(j['datetime'][0:4])
comp_month = int(j['datetime'][5:7])
comp_day = int(j['datetime'][8:10])
comp_hour = int(j['datetime'][11:13])
comp_minute = int(j['datetime'][14:16])
if task == input_task:
if (comp_year==date_year):
if comp_month == date_month:
if comp_day == date_day:
if comp_hour == time_hour:
if comp_minute <= time_minute:
tasks[n]['completion'] = 2
n = n+1
break
elif comp_hour < time_hour:
tasks[n]['completion'] = 2
n = n+1
break
elif comp_day < date_day:
tasks[n]['completion'] = 2
n = n+1
break
elif comp_month < date_month:
tasks[n]['completion'] = 2
n = n+1
break
elif comp_year < date_year:
tasks[n]['completion'] = 2
n = n+1
break
else:
if (cur_year==date_year):
if cur_month == date_month:
if cur_day == date_day:
if cur_hour == time_hour:
if cur_minute <= time_minute:
tasks[n]['completion'] = 1
n = n+1
continue
elif cur_hour < time_hour:
tasks[n]['completion'] = 1
n = n+1
continue
elif cur_day < date_day:
tasks[n]['completion'] = 1
n = n+1
continue
elif cur_month < date_month:
tasks[n]['completion'] = 1
n = n+1
continue
elif cur_year < date_year:
tasks[n]['completion'] = 1
n = n+1
continue
tasks[n]['completion'] = 0
n = n+1
print(tasks)
print(comp_tasks)
return render_template('display_input.html',data=tasks)
except FileNotFoundError:
return "NO TASKS"
@app.route('/reset/',methods=['POST'])
def reset(filename = 'input_task.json'):
if os.path.exists(filename):
os.remove(filename)
return 'reset complete'
#@app.route('/delete/')
#def delete(filename = 'rfid_data.json'):
# global process
# process.terminate()
# process.wait()
# process = subprocess.Popen(['python3', 'update_rfid_data.py'])
# return 'deletion complete'
if __name__ == '__main__':
app.run(debug=True, host='0.0.0.0')
