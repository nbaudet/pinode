# Dev installation of backend

First render the install scripts executable, then make sure that Python3, pip and virtualenv are installed and install RabbitMQ on your system:

```shell
$ chmod +x scripts/* && make install-reqs
```

Make sure that RabbitMQ was installed correctly by going to `http://localhost:15672/`. You should see the RabbitMQ login screen.

Note: The script did not create a vhost, letting this option to you.

The default user and password are `guest`. this account is only available from localhost, and you should change them if you plan to use RabbitMQ from other machines on your network.

Note: If you would like to set another account, remember to select a vhost and give it the according privileges by clicking the **Set permission** button, in the Admin section of RabbitMQ

## Virtual environment

1. Create a virtual environment called 'pinode-env' defining the version of Python you want to use:\
`$ virtualenv -p /usr/bin/python3 pinode-env`

2. Activate the virtual environment 'pinode-env' with:\
`$ source pinode-env/bin/activate`\
Note: You might need to type the following in order to make the script executable:\
`$ chmod +x pinode-env/bin/activate`

    Note: If needed, you can deactivate it with `$ deactivate`.

## Dependencies
Install the dependencies inside your virtual environment with:\
`(pinode-env) $ pip install -r requirements.txt`


## Database and admin user
As in any Django app, apply migrations and create a super user:
```shell
$ python manage.py migrate
$ python manage.py createsuperuser
```

## Register the current node
Fill the app's database with your current machine, and describe it as "is_self" = True, so the sensors know which node they are installed onto.

You have to give it a name. The name shouldn't contain any special characters.

```shell
$ python manage.py registerself "<nodename>"
```

## Run the Django server
Type: `$ python manage.py runserver` or `$ make run` if your system supports Makefiles.

Then you can login at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) with the superuser you just created.

## Dev installation of frontend

...
#
## Run tests
`$ python manage.py test`