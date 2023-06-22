# Ctruh Task Backend Assignment #
The main project resides in task/ directory.

## Instructions to run the app locally: ##
* Clone the repo, install the requirements and move to this directory
  * `git clone https://github.com/Ankit-Somani/ctruh-assignment.git`
  * `pip install -r requirements.txt`
  * `cd ctruh-assignment/task` 
* Run the django app
  * `python manage.py runserver`
* Copy the url shown in the terminal and open it in a browser.
  * http://127.0.0.1:8000/app/register : To register as a user, send a post request at this route with username and password as json, it will return a token. This token must be copied and sent as header in the request. Request body sample: { 'username' : 'user', 'password' : '1234'} and header with token should be sent as shown in the image:
    
    ![image](https://github.com/Ankit-Somani/ctruh-assignment/assets/82326089/d545f716-a287-49f0-85bd-6df1fed39b9d)

  * http://127.0.0.1:8000/app/tasks/: returns all the tasks currently in the database
  * http://127.0.0.1:8000/app/tasks/remaining: returns all the tasks with status incomplete
  * http://127.0.0.1:8000/app/tasks/pk: return the task with task number = pk (replace pk to some integer in the route)
  * http://127.0.0.1:8000/app/tasks/create: make a POST request at this route to create a task with request body like: {'task_no': 5, 'task_name': 'write readme', 'due_date': '2023-06-23', 'completed': 0}
  * http://127.0.0.1:8000/app/tasks/update/pk: make PATCH request at this route to update a task with task number = pk (replace pk to some integer in the route) and body as above excluding task_no field
  * http://127.0.0.1:8000/app/tasks/delete/pk: make DELETE request at this route to delete a task with task number = pk (replace pk to some integer in the route)
  * http://127.0.0.1:8000/app/tasks/complete/pk: make PATCH request at this route to mark a task complete with task number = pk (replace pk to some integer in the route)
  
* About the fields of model Task:
  * task_no: Unique number for each task starting from 1 (integer)
  * task_name: Display name of the task (string)
  * due_date: Due date of the task (DateField, date in the format 'YYYY-MM-DD')
  * completed: Status of the task (boolean)
  
