Pycon Canada 2015
=================


Development Environment Setup
-----------------------------

You will need the following:

- [Python 3.4+](https://www.python.org/downloads/)
- [npm](https://www.npmjs.org/)
- [pip](https://pip.pypa.io/en/stable/)
- [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)

Start by creating a python virtual environment:

    $ npm install
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

    
    import os
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
    DEBUG = True
    TEMPLATE_DEBUG = True
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'dev_db.sqlite3'),
        }
    }

Run the project:

    (pycon) $ python manage.py runserver


Less Styles Compilation
-----------------------

Gulp is used to watch and autorun less compilation:

    $ gulp
