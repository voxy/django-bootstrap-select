from django.contrib.staticfiles.templatetags.staticfiles import static
from django import forms
from django.forms import Select
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class BootstrapSelect(Select):

    @property
    def media(self):
        return forms.Media(
            css={
                'all': ('//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css',
                        '//cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.12.4/css/bootstrap-select.min.css',  # noqa
                        static('bootstrap_select/bootstrap_select.css'),)
            },
            js=('//ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js',
                '//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js',
                '//cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.12.4/js/bootstrap-select.min.js',)  # noqa
        )

    def __init__(self, attrs=None, choices=()):
        if attrs is None:
            attrs = {'class': 'selectpicker'}
        else:
            try:
                attrs['class'] += ' selectpicker'
            except KeyError:
                attrs['class'] = 'selectpicker'
        super(BootstrapSelect, self).__init__(attrs=attrs, choices=choices)

    # Django 1.8
    def render_option(self, selected_choices, option_value, option_label):
        if option_value is None:
            option_value = ''
        option_value = force_text(option_value)
        if option_value in selected_choices:
            selected_html = mark_safe(' selected="selected"')
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        else:
            selected_html = ''
        return format_html('<option value="{}" data-content="{}" {}>{}</option>',
                           option_value,
                           force_text(option_label),
                           selected_html,
                           force_text(option_label),)

    # Django 1.11
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super(BootstrapSelect, self).create_option(name, value, label, selected,
                                                            index, subindex=None, attrs=None)
        option['attrs']['data-content'] = label
        return option
