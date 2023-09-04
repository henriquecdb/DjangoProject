from .settings import *
import os

DEBUG = True

SECRET_KEY = 'h#!h++#=&6vg$q(ii@8b4a6)d_b=ujhm=_-(^4%s%400bvv07='

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


