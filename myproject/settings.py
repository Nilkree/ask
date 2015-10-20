# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket

BASE_DIR = os.path.dirname(os.path.dirname(__file__))




# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')_7av^!cy(wfx=k#3*7x+(=j^fzv+ot^1@sh9s9t=8$bu@r(z$'

# SECURITY WARNING: don't run with debug turned on in production!
# adjust to turn off when on Openshift, but allow an environment variable to override on PAAS
try:
    from myproject.local_settings import *
    DEBUG = True
except:
    DEBUG = False


ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'loginsys',
    'website',
    
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

)

ROOT_URLCONF = 'myproject.urls'
WSGI_APPLICATION = 'myproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

try:
    from myproject.local_settings import *
except:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'mydb',
            'USER': 'shop',
            'PASSWORD': 'NDcwYWE0NjAxNjZkYjZlYzBiN2IwMDNk',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
'''
try:
    from myproject.local_settings import *
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
    MEDIA_ROOT =  os.path.join(BASE_DIR, 'media/')
except:
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static/')
    MEDIA_ROOT =  os.path.join(os.path.dirname(BASE_DIR), 'media/')
'''
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static/')
MEDIA_ROOT =  os.path.join(os.path.dirname(BASE_DIR), 'media/')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR,"static"),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
'''
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.core.context_processors.request",
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates'),
)
'''
LOGIN_URL = '/auth/login/'

ADMINS = (
    ('nilkree', 'lyubatskiy.dima@gmail.com'),
)
'''
DEFAULT_EMAIL_FROM = 'shoplifter1234@gmail.com'
DEFAULT_EMAIL_BCC = ''

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'shoplifter1234@gmail.com'
EMAIL_HOST_PASSWORD = 'Oj3k9tu34l'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
SERVER_EMAIL = 'shoplifter1234@gmail.com'
'''


