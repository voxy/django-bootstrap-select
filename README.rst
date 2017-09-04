=============================
Django Bootstrap Select
=============================

.. image:: https://badge.fury.io/py/django-bootstrap-select.svg
    :target: https://badge.fury.io/py/django-bootstrap-select

.. image:: https://travis-ci.org/voxy/django-bootstrap-select.svg?branch=master
    :target: https://travis-ci.org/voxy/django-bootstrap-select

.. image:: https://codecov.io/gh/voxy/django-bootstrap-select/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/voxy/django-bootstrap-select

A Django wrapper for the Bootstrap Select library

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

Using it in a form:

.. code-block:: python

    def get_choices():
        choices = (('face.jpg', escape('<img src="path-to-face.jpg"/>'),)
        return choices

    class IconForm(forms.Form):
        icon = forms.URLField(widget=BootstrapSelect(choices=get_choices()))

Features
--------

* Renders labels from form choices as `custom-content`_.

.. _`custom-content`: https://silviomoreto.github.io/bootstrap-select/examples/#custom-content

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
