# pycon-2015

Pycon Canada 2015
=================


Development Environment Setup
-----------------------------

You will need the following:

- Python 3.4+

Start by creating a python virtual environment:

    $ mkvirtualenv pycon --python=/usr/local/bin/python3
    (pycon) $

The `(pycon)` prefix indicates that a virtual environment called "pycon" is being used. Next, check that you have the correct version of Python:

    (pycon) $ python --version
    Python 3.4.3
    (pycon) $ pip --version
    pip 7.1.1 from /Users/..../site-packages (python 3.4)

Install the project requirements:

    (pycon) $ pip install --upgrade -r requirements.txt

Create the database:

    (pycon) $ python manage.py migrate

Create `pycon/localsettings.py` with the following

    DEBUG = True
    TEMPLATE_DEBUG = True
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

Run the project:

    (pycon) $ python manage.py runserver
