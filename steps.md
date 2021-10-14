1. mkdir project
2. python3 -m venv venv
3. source venv/bin/activate
4. install dependencies
pip install django
pip install gunicorn django-heroku
python -m pip install Pillow
5. django-admin startproject ideal_villa .
6. python manage.py startapp stock
8. in ideal_villa/setting.py add stock in INSTALLED_APP
9. Create the models
11. python3 manage.py makemigrations
12. python3 manage.py migrate
13. python3 manage.py createsuperuser
admin/admin
14. python3 manage.py runserver
15. pipreqs
16. add .gitignore
17. add Procfile
--------------HEROKU---------------
1. Create procfile
2. in seetings set DEBUG to Fasle

 heroku run python3 manage.py makemigrations --app villa-ideal
 heroku run python3 manage.py migrate --app villa-ideal
 heroku run python3 manage.py createsuperuser --app villa-ideal

 heroku logs --tail --app villa-ideal
 heroku restart --app villa-ideal

django_heroku==0.3.1
django_summernote==0.8.11.6
Django==2.2.12
gunicorn==20
Pillow==8.3.2

