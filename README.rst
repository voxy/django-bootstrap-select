=============================
Django Bootstrap Select
=============================

.. image:: https://badge.fury.io/py/django-bootstrap-select.svg
    :target: https://badge.fury.io/py/django-bootstrap-select

.. image:: https://travis-ci.org/massover/django-bootstrap-select.svg?branch=master
    :target: https://travis-ci.org/massover/django-bootstrap-select

.. image:: https://codecov.io/gh/massover/django-bootstrap-select/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/massover/django-bootstrap-select

A wDjango wrapper for the Bootstrap Select library

Documentation
-------------

The full documentation is at https://django-bootstrap-select.readthedocs.io.

Quickstart
----------

Install Django Bootstrap Select::

    pip install django-bootstrap-select

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'bootstrap_select.apps.BootstrapSelectConfig',
        ...
    )

Add Django Bootstrap Select's URL patterns:

.. code-block:: python

    from bootstrap_select import urls as bootstrap_select_urls


    urlpatterns = [
        ...
        url(r'^', include(bootstrap_select_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
