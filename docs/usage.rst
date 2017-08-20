=====
Usage
=====

To use Django Bootstrap Select in a project, add it to your `INSTALLED_APPS`:

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
