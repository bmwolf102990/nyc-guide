# NYC Guide

**Created By:**

- Bryan Wolf ( *GitHub @ bmwolf102990* )
- Christy Hayter ( *GitHub @ Christy131* )


## Summary

Users can explore New York City's famous five boroughs! Click on a chosen borough to see what noteworthy attractions and activites can be found there. Next, click on an attraction/activity to see a more specific list of related venue options. Finally, click on any venue to view in-depth background info and other details about it.

**HAVE FUN EXPLORING NYC!**


### Setting Up A Virtual Enviorment And Using Django

> ***NOTE:*** If you are trying to get started using a cloned repo created by someone else, follow steps 1 & 2 
> to set up your virtual environment, than run the following line in your terminal:
>
> `pip install -r requirements.txt`

1. Set up virtual environment from terminal using the following command:

> `python3 -m venv venv`
>
> ***NOTE:*** If `python3` does not work on your computer, try using either `python` or `py`

2. Activate your new virtual environment using one of the following commands:

> **For Mac & Linux:** `source venv/bin/activate`
>
> **For Windows:** `venv\Scripts\activate`

3. Add a `.gitignore` file.

>***NOTE:*** A good `.gitignore` file template for python/django can be found [here](https://github.com/github/gitignore/blob/main/Python.gitignore)

4. Install Django: 

> `pip install django`

5. Create a `requirements.txt` file:

> `pip freeze > requirements.txt`

5. Create a Django project:

> `django-admin startproject <project-name>`

6. Run your server to make sure it is working correctly: 

> `python3 manage.py runserver`

7. Create an app inside your project:

> `python3 manage.py startapp <app name>`

8. Install your new app in your project's `settings.py` file (by adding the configuration from the `apps.py` file)
