from django.contrib import admin
from django import forms
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import escape

from .models import Icon
from bootstrap_select import BootstrapSelect


def get_choices():
    filenames = ['face.jpg', 'dog.jpg', ]
    choices = []
    for filename in filenames:
        src = static('example_app/{}'.format(filename))
        label = '<img src="{}"/>'.format(src)
        choices.append((filename, escape(label)))
    return choices


class IconAdminForm(forms.ModelForm):
    icon = forms.URLField(widget=BootstrapSelect(choices=get_choices(),))

    class Meta:
        model = Icon
        fields = ('icon', 'name', )


@admin.register(Icon)
class IconAdmin(admin.ModelAdmin):
    form = IconAdminForm
