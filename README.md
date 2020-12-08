# Kuki-shop

An E-Commerce site for a medium size business, built using Python/Django, Bootstrap and React. still under development
customers to shop for textile materials as guest or as registered users.

![screenshot_2020-12-07-kuki-tex](https://user-images.githubusercontent.com/10378288/101414713-e759fd00-38e6-11eb-8482-51ef2104f0db.jpg)

## Key Features

* checkout form
* cart section
* user authentication
* async task spooling
* textile categories
* shop as a guest without registration

![Screenshot_2020-12-03 Kuki-Textiles](https://user-images.githubusercontent.com/10378288/101415017-736c2480-38e7-11eb-952a-aa1f747895e3.png)

## Technology stack

* Django
* jQuery and Ajax
* Bootstrap
* Allauth

## Setup

* clone the project
* create and start a virvual env
* Install project dependencies 
`
pip install -r requirements.txt
`
* you might as well setup your secret key, here we use windows env
* create your database and add to settings.py
`run 'python manage.py migrate'`
* create admin account \
`run 'python manage.py makemigrations`
`run 'python manage.py migrate'`
* to start dev server 
`run 'python manage.py runserver'`

# Dependencies

* weezyprint
* pytz
* crispyform
* django-allauth
* braintree
* celery

# How To Contribute

fork the project and follow the setup process
