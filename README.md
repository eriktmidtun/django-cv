# django-cv
This is my personal website www.erikmidtun.no hosted on Heroku [20.08.2020]

Frontend is built with django templates and Bootstrap/CSS
Backend adminpanel is from Django 3.1

This gives me the ability to update my cv on my site fast and easily.

### Use
Admin panel have models:

* Section
* Entry
* Sidebar section
* Sidebar entry

url/admin is for admin panel. need a superuser for this.

In the admin panel there is options for:

* Ordering Sections and entries

    * Order priority index. higher number higher up.

* show and hide sections and entries.

### *Prereq*
You need Python 3 and pip: [Python 3 og pip](https://www.python.org/downloads/).

### *installation*

Install virtualenv with pip

```bash
pip3 install virtualenv
```

Activate virtual environment 
```bash
#For Windows

virtualenv venv                      
venv\Scripts\activate                
```
```bash
#For Mac/Linux

virtualenv -p python3 venv          
venv/bin/activate                 
```
Install pip-modules in virtualenv
```bash
pip install -r requirements.txt
```
Set up databasemodels
```bash
python manage.py migrate
```
Setup a superuser.
```bash
python manage.py createsuperuser
```

setup static files
```bash
python manage.py collectstatic
```

