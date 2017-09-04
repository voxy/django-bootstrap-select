#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import SimpleTestCase
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

    def test_it_allows_additional_class_attrs(self):
        class ExampleForm(forms.Form):
            icon = forms.URLField(
                widget=BootstrapSelect(choices=self.CHOICES,
                                       attrs={'class': 'hello-world'})
            )

        form = ExampleForm()
        class_html = 'class="hello-world selectpicker"'
        self.assertIn(class_html, form.as_p())
