# BLOG APP
## 1. Create an app
    py manager.py startapp <app_name>    

## 2. Migrations

- ### Create migrations
````
    python manage.py makemigrations <app_name> 
````
- ### sqlmigrate, which displays the SQL statements for a migration.

````
    python manage.py sqlmigrate <app_name> <migration_name> 
````
- ### Apply migrations

````
python manage.py migrate
````
- ### Create a super User
````
    python manager.py createsuperuser
````