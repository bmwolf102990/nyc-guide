"# nyc-guide." 


### Summary
allows user to click on a borough,which takes them to links to the activities for that bouough and in each activity there are links to each venue for the activities.


#### Setting up a Virtual Enviorment and using Django
1. Step up virtual environment ‘python3 -m venv venv
2. activate it. ‘source venv/bin/activate’
3. Add a .gitignore
4. Install Django ‘pip install django’ then run ‘pip freeze > requirements.txt’
5. create a Django project with ‘django-admin startproject "project-name"’
6. Run python manage.py run server (to see if it worked) python3 manage.py runserver
7. Create an app inside your project with “python manage.py startapp 'app name'"
8. Install your new app in your project’s settings file (by adding the configuration from the apps.py
9. Add to main urls.py and add the path
10. Follow the steps to create and send web responses. using the views.py, urls.py creating html templates for each page in the app file. Also linking the app to the main mysite folder in urls and settings