=====
Usage
=====

Custom Content
==============

The BootstrapSelect widget will take the labels from choices and render
them as `custom-content`_

.. code-block:: python

    def get_choices():
        choices = (('face.jpg', escape('<img src="path-to-face.jpg"/>'),)
        return choices

    class IconForm(forms.Form):
        icon = forms.URLField(widget=BootstrapSelect(choices=get_choices()))

.. _`custom-content`: https://silviomoreto.github.io/bootstrap-select/examples/#custom-content


Live Search
===========

Adding the `data-live-search` attribute to the widget enables `live-search`_. It
will take values and load them in as tokens so they are searchable.

.. note:: `bootstrap-select` expects the attribute to be `data-live-search="true"`

.. code-block:: python

    class ExampleForm(forms.Form):
        icon = forms.URLField(
                widget=BootstrapSelect(choices=self.CHOICES,
                                       attrs={'data-live-search': 'true'})
        )

.. _`live-search`: https://silviomoreto.github.io/bootstrap-select/examples/#live-search

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
