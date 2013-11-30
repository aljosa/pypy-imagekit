django-imagekit on PyPy
=

Example Django project w/ django-imagekit running on PyPy 2.2.1 and results in ImportError but works on CPython 2.7.x.


**PyPy version (Ubuntu 13.04; from PyPy PPA):**

    Python 2.7.3 (2.2.1+dfsg-1~ppa1, Nov 28 2013, 02:02:56)
    [PyPy 2.2.1 with GCC 4.6.3] on linux2

**Steps to reproduce error:**

1) git clone this repo:

    $ git clone git://github.com/aljosa/pypy-imagekit
    $ cd pypy-imagekit

2) create and activate virtualenv w/ pypy:

    $ virtualenv -p pypy env
    $ . env/bin/activate

3) use pip to install requirements from requirements.txt:

    $ pip install -r requirements.txt

4) source profile file, it sets DJANGO_SETTINGS_MODULE and PYTHONPATH:

    $ . profile

5) run django-admin.py runserver:

    $ django-admin.py runserver

6) open http://localhost:8000 in browser:

    $ xdg-open http://localhost:8000
