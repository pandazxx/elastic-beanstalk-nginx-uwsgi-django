# -*- coding: UTF-8 -*-

import environ
from .base_settings import *


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

_current_path = environ.Path(__file__)
project_root = _current_path - 2


ALLOWED_HOSTS = [
    '*'
]

INSTALLED_APPS = [
    'ebsample_app.apps.EbsampleAppConfig',
    'grappelli',
] + INSTALLED_APPS


STATIC_ROOT = project_root('static')
