from django.conf import settings
from django.core.signals import setting_changed

_bootstrap_select_assets = getattr(settings, 'BOOTSTRAP_SELECT_ASSETS', {})

_default_assets = {
    'bootstrap_js': True,
    'bootstrap_css': True,
    'jquery_js': True,
}

BOOTSTRAP_SELECT_ASSETS = {
    'bootstrap_js': _bootstrap_select_assets.get('bootstrap_js', _default_assets['bootstrap_js']),
    'bootstrap_css': _bootstrap_select_assets.get('bootstrap_css', _default_assets['bootstrap_css']),  # noqa
    'jquery_js': _bootstrap_select_assets.get('jquery_js', _default_assets['jquery_js']),
}


def reload_settings(*args, **kwargs):
    global BOOTSTRAP_SELECT_ASSETS
    setting, value = kwargs['setting'], kwargs['value']
    if setting == 'BOOTSTRAP_SELECT_ASSETS':
        if value is None:
            value = {}

        BOOTSTRAP_SELECT_ASSETS = {
            'bootstrap_js': value.get('bootstrap_js', _default_assets['bootstrap_js']),
            'bootstrap_css': value.get('bootstrap_css', _default_assets['bootstrap_css']),
            'jquery_js': value.get('jquery_js', _default_assets['jquery_js']),
        }


setting_changed.connect(reload_settings)
