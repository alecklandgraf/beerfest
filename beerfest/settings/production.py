# Django settings for beerfest project.
from beerfest.settings.common import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

import dj_database_url
DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['*']
