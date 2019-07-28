# Dev installation of backend

First make sure that Python3, pip and virtualenv are installed on your system.

## Virtual environment
1. Install virtualenv if you want to manage dependencies in a virtual environment:\
`$ sudo apt install virtualenv`

2. Then create a virtual environment called 'pinode-env' defining the version of Python you want to use:\
`$ virtualenv -p /usr/bin/python3 pinode-env`

3. Activate the virtual environment 'pinode-env' with:\
`$ source pinode-env/bin/activate`\
Note: You might need to type the following in order to make the script executable:\
`$ chmod +x pinode-env/bin/activate`

    Note: If needed, you can deactivate it with `$ deactivate`.

## Dependencies
Install the dependencies inside your environment with:\
`(pinode-env) $ pip install -r requirements.txt`


## Database and admin user
As in any Django app, apply migrations and create a super user:
```
$ python manage.py migrate
$ python manage.py createsuperuser
```

## Run the Django server
Type: `$ python manage.py runserver` or `$ make run` if your system supports Makefiles.

Then you can login at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) with the superuser you just created.

## Dev installation of frontend

...
#
## Run tests
`$ python manage.py test`