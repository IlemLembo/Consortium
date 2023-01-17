import os
"""
Django settings for webapp project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y(h05ytb$a5zy^9lek&y7g&3#ftqbrt0__be-g**5hoi7erb%e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["192.168.1.64", "127.0.0.1", "192.168.1.66", "localhost"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication',
    'music',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'webapp.urls'
temp = os.path.join(BASE_DIR, 'authentication/templates/' )
TEMPLATES_DIR = [
    os.path.join(BASE_DIR, 'authentication/templates/'),
    os.path.join(BASE_DIR, 'music/templates/'),
    os.path.join(temp, 'authentication/'),
    os.path.join(temp, 'home/'),
    os.path.join(temp, 'registration/'),
    ]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATES_DIR,
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

WSGI_APPLICATION = 'webapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lamba',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': "127.0.0.1",
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR.joinpath('static/')
STATICFILES_DIRS = [
    os.path.join(STATIC_ROOT, 'admin/css'),
    os.path.join(STATIC_ROOT, 'admin/'),
    os.path.join(STATIC_ROOT, 'admin/img'),
    os.path.join(STATIC_ROOT, 'admin/fonts'),
    os.path.join(STATIC_ROOT, 'admin/js'),
    os.path.join(STATIC_ROOT, 'css'),
    os.path.join(STATIC_ROOT, 'img'),
    os.path.join(STATIC_ROOT, 'scripts'),
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#LOGIN_URL = 'login'
# LOGIN_REDIRECT_URL = 'home'
#LOGOUT_REDIRECT_URL = 'login'
AUTH_USER_MODEL = 'authentication.User'
MEDIA_URL = 'media/'
MEDIA_ROOT= BASE_DIR.joinpath('media/')

# SMTP configuration

from django.core.mail import send_mail

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'lemboilem@gmail.com'
EMAIL_HOST_PASSWORD = 'ccqxquotduwwiimu'


# PAYGATE DATA :

PAYGATE_URL = "https://paygateglobal.com/api/v1/pay"

API_KEY = "86a33614-3018-41c0-9d1c-bafc86f2e5fd"