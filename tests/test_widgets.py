#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import SimpleTestCase, override_settings
from django import forms

from bootstrap_select import BootstrapSelect


class TestBootstrapSelect(SimpleTestCase):
    CHOICES = (('face', 'example.com/face.jpg'),)

    def test_it_adds_data_content_from_choices(self):
        class ExampleForm(forms.Form):
            icon = forms.URLField(widget=BootstrapSelect(choices=self.CHOICES))

        form = ExampleForm()
        option_html = ('<option data-content="example.com/face.jpg" value="face" >'
                       'example.com/face.jpg</option>')
        self.assertInHTML(option_html, form.as_p())

    def test_it_adds_tokens_for_search_if_live_search_attribute_is_set(self):
        class ExampleForm(forms.Form):
            icon = forms.URLField(widget=BootstrapSelect(
                choices=self.CHOICES,
                attrs={'data-live-search': "true"},
            ))

        form = ExampleForm()
        option_html = ('<option data-content="example.com/face.jpg" '
                       ' data-tokens="face" value="face" >'
                       'example.com/face.jpg</option>')
        self.assertInHTML(option_html, form.as_p())

    def test_it_allows_additional_class_attrs(self):
        class ExampleForm(forms.Form):
            icon = forms.URLField(
                widget=BootstrapSelect(choices=self.CHOICES,
                                       attrs={'class': 'hello-world'})
            )

        form = ExampleForm()
        class_html = 'class="hello-world selectpicker"'
        self.assertIn(class_html, form.as_p())

    def test_default_media_css(self):
        class ExampleForm(forms.Form):
            icon = forms.URLField(widget=BootstrapSelect(choices=self.CHOICES))

        form = ExampleForm()
        links = list(form.media.render_css())
        self.assertEqual(len(links), 3)

        scripts = list(form.media.render_js())
        self.assertEqual(len(scripts), 3)

    def test_it_allows_kwargs_for_assets(self):
        class ExampleForm(forms.Form):
            icon = forms.URLField(
                widget=BootstrapSelect(choices=self.CHOICES,
                                       bootstrap_js=False,
                                       bootstrap_css=False,
                                       jquery_js=False,)
            )

        form = ExampleForm()

        links = list(form.media.render_css())
        self.assertEqual(len(links), 2)

        scripts = list(form.media.render_js())
        self.assertEqual(len(scripts), 1)

    ALL_FALSE_ASSETS = {
        'bootstrap_js': False,
        'bootstrap_css': False,
        'jquery_js': False,
    }

    @override_settings(BOOTSTRAP_SELECT_ASSETS=ALL_FALSE_ASSETS)
    def test_it_allows_django_settings_for_assets(self):
        class ExampleForm(forms.Form):
            icon = forms.URLField(widget=BootstrapSelect(choices=self.CHOICES))

        form = ExampleForm()

        links = list(form.media.render_css())
        self.assertEqual(len(links), 2)

        scripts = list(form.media.render_js())
        self.assertEqual(len(scripts), 1)
