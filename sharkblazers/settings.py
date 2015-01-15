"""
Django settings for the project.
"""

import os
from sharkblazers.configurator import Configurator

#PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
config = Configurator(os.path.abspath(os.path.join(os.path.dirname(__file__))))

PROJECT_PATH = config.workspace
SECRET_KEY = config.secret_key
DEBUG = config.debug
TEMPLATE_DEBUG = DEBUG
APP_URL = config.get("APP_URL")
ALLOWED_HOSTS = config.get("ALLOWED_HOSTS")
ADMINS = config.get("ADMINS")


## DEFAULTS
ROOT_URLCONF = 'sharkblazers.urls'
WSGI_APPLICATION = 'sharkblazers.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'


EMAIL_HOST = config.get("SMTP")["host"]
EMAIL_PORT = config.get("SMTP").get("port", None)
EMAIL_USERNAME = config.get("SMTP").get("username", None)
EMAIL_PASSWORD = config.get("SMTP").get("password", None)
EMAIL_DEFAULT_ADDRESS = config.get("SMTP").get("default_address", None)

if config.contains("LOGGING"):
    LOGGING = config.get("LOGGING")

if config.contains("DATABASES"):
    DATABASES = config.get("DATABASES")


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'faker'
)


# INSTALLED_APPS = (
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'south',
#     'core',
#     'accounts',
#     'captcha',
#     'block_ip',
# )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)