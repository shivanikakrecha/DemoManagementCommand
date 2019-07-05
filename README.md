# DemoManagementCommand
This project is for get data from api using management command script. 

Installtion step:-

**step-1** Clone repo.

**step-2** Create virtual environment using **virtualenv -p python3 venv**

**step-3** Install requirements using command **pip install -r requirements.txt**

**step-4** Run python server

**step-5** Apply migration using **python manage.py migrate**.

**step-6** Create superuser using command **python manage.py createsuperuser** or **./manage.py createsuperuser**


Now its time to run management command.

You can see all the commands which are using with python manage.py <command>. using python manage.py --help.

Into this we are going to run command python manage.py api_get_data.

The above command retrive all data from api which is mentioned into DemoManagementCommand -> snippets -> management -> commands -> api_get_data.py.


