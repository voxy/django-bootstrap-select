=====
Usage
=====

Assets
======

If you do not want some of the assets provided, there are two options:

Assets can be controlled globally through `settings`:

.. code-block:: python

    BOOTSTRAP_SELECT_ASSETS = {
        'bootstrap_js': False,
        'bootstrap_css': False,
        'jquery_js': False,

    }


Assets can also be declared as widget kwargs:

.. code-block:: python

    class ExampleForm(forms.Form):
        icon = forms.URLField(
                widget=BootstrapSelect(choices=self.CHOICES,
                                       bootstrap_js=False,
                                       bootstrap_css=False,
                                       jquery_js=False,)
        )
