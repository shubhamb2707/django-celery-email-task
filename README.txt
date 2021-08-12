## Python version 3.6.9

## Create Virtual environment and install all the dependencies using following command
```
pip install -r requirements.txt
```

## Run Following commands to migrate models into db:
```
python manage.py migrate
```

## create admin user using following command : 
```
python manage.py createsuperuser
```

## Run Celery worker using following command : 
```
celery -A cis_task.celery worker -l info
```

## Run server using following command : 
```
python manage.py runserver
```

To test the application follow these steps : 

1 Go to browser and hit 127.0.0.1:8000 to access the homepage.
2 On homepage you will see options to create users, from there create some users and check in admin panel if users are creaeted successfully.
3. Now go back to homepage and click on send emails button, this will send email to all the existing users. You can check it by either celery worker terminal.
4. Hit "mailinator.com" on browser and open inbox, copy any email id from django-admin panel and paste it on search bar in mailinator. You should see the customized email you sent from application, also you can see the "sent mail" on gmail.
Gmail creds are as follows : 
email : newslettersheep.project@gmail.com
password : news@12345

[Note :  You can also export your personal gmail creds using .env file, but you have to make changes in mail setting security.]



