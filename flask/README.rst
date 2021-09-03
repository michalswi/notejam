**************
Notejam: Flask
**************

Notejam application implemented using `Flask <http://flask.pocoo.org/>`_ microframework.

Flask version: 1.1.1  

Docker image: michalsw/notejam-k8s  

Flask extension used:

* Flask-Login
* Flask-Mail
* Flask-SQLAlchemy
* Flask-Testing
* Flask-WTF

==========================
Run in docker
==========================
Please use **make**:

.. code-block:: bash

    $ make
    Usage:
    make <target>

    Targets:
    build            Build docker image
    run              Create docker volume and run docker container
    logs             Get logs from docker container
    stop             Stop docker container and remove docker volume


==========================
Installation and launching
==========================

-----
Clone
-----

Clone the repo:

.. code-block:: bash

    $ git clone git@github.com:nordcloud/notejam.git YOUR_PROJECT_DIR/

-------
Install
-------
Use `virtualenv <http://www.virtualenv.org>`_ or `virtualenvwrapper <http://virtualenvwrapper.readthedocs.org/>`_
for `environment management <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_.

Install dependencies:

.. code-block:: bash

    $ cd YOUR_PROJECT_DIR/flask/
    $ pip install -r requirements.txt

Create database schema:

.. code-block:: bash

    $ cd YOUR_PROJECT_DIR/flask/
    $ python db.py

------
Launch
------

Start flask web server:

.. code-block:: bash

    $ cd YOUR_PROJECT_DIR/flask/
    $ python runserver.py

Go to http://127.0.0.1:5000/ in your browser

---------
Run tests
---------

Run functional and unit tests:

.. code-block:: bash

    $ cd YOUR_PROJECT_DIR/flask/
    $ python tests.py


============
Contribution
============

Do you have python/flask experience? Help the app to follow python and flask best practices.

Please send your pull requests in the ``master`` branch.
Always prepend your commits with framework name:

.. code-block:: bash

    Flask: Implemented sign in functionality

Read `contribution guide <https://github.com/komarserjio/notejam/blob/master/contribute.rst>`_ for details.
