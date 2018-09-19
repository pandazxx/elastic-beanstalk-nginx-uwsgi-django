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


STATIC_ROOT = project_root('static')
