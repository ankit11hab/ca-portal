"""
Django settings for ca_portal project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from django.contrib.messages import constants as messages


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1x$%_n-6&+^ch=_6j)0kg+5*1p0=ri#*b)g1=ge8f8#-(8)9rb'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
# ALLOWED_HOSTS = ["localhost"]

DEBUG = True
ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'crispy_forms',
    'phonenumber_field',
    'mathfilters',
    'ca_portal',
    'dashboard.apps.DashboardConfig',
    'users.apps.UsersConfig',
    'submissions.apps.SubmissionsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'ca_portal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': [
#             'profile',
#             'email',
#         ],
#         'AUTH_PARAMS': {
#             'access_type': 'online',
#         },
#         'APP': {
#             'client_id': '764894753807-svtfck5d56i3od79g1paj5ls6amkms0p.apps.googleusercontent.com',
#             'secret': '-uxKcTO4s3L3ADX4oZgtXZPd',
#         }
#     }
# }

WSGI_APPLICATION = 'ca_portal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'error',
}

LOGOUT_REDIRECT_URL = 'dashboard_page'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
# DEFAULT_FILE_STORAGE = "minio_storage.storage.MinioMediaStorage"
# STATICFILES_STORAGE = "minio_storage.storage.MinioStaticStorage"
# MINIO_STORAGE_ENDPOINT =os.environ.get('minio_endpoint')
# MINIO_STORAGE_ACCESS_KEY = os.environ.get('minio_access')
# MINIO_STORAGE_SECRET_KEY = os.environ.get('minio_secret')
# MINIO_STORAGE_USE_HTTPS = True
# MINIO_STORAGE_MEDIA_BUCKET_NAME = 'alchercamedia'
# MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True
# MINIO_STORAGE_STATIC_BUCKET_NAME = 'alchercastatic'
# MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = True
MEDIA_URL = '/image-uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'image-uploads')
CRISPY_TEMPLATE_PACK = 'bootstrap4'


AUTH_USER_MODEL = 'users.NewUser'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

SECURE_REFERRER_POLICY = "no-referrer-when-downgrade"
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
