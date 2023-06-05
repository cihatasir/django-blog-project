# Django Blog App
## Installation
```
git clone https://github.com/cihatasir/django-blog-project.git
```

## Install Dependencies
```
pip install -r requirements.txt
```

## Set Database
```
python3 manage.py makemigrations
python3 manage.py migrate
```

## If No Such Table
```
python3 manage.py migrate --run-syncdb
```

## Create SuperUser
```
python3 manage.py createsuperuser
```

## Run Server
```
python3 manage.py runserver
```

After all these steps, you can start testing and developing this project.