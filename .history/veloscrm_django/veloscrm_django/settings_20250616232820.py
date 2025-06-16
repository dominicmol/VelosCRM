from pathlib import Path  # voor padmanipulatie zonder os.path
import os                 # omgevingsvariabelen instellen

# basisdirectory van je project
BASE_DIR = Path(__file__).resolve().parent.parent

# geheime sleutel en debug-instelling (NOOIT in productie zo laten staan)
SECRET_KEY = 'django-insecure-wn_v7z89$xlu+@uyo@um7_0mzlbcc_m$i$6x5+(#tx)3j%%auy'
DEBUG = True

# hosts die je site mogen benaderen
ALLOWED_HOSTS = ['*']

# CSRF- en CORS-instellingen voor externe frontends
CSRF_TRUSTED_ORIGINS = [
    'https://dominicmol.pythonanywhere.com',
]
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8080',
    'http://localhost:8081',
    'http://localhost:8082',
    'https://sweet-pegasus-376b81.netlify.app',
]
CORS_ALLOW_CREDENTIALS = True  # stuur cookies en credentials mee

# ingeschakelde Django- en externe apps
INSTALLED_APPS = [
    # Django-basis
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # externe pakketten
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'django_filters',
    'django_extensions',

    # eigen apps
    'client.apps.ClientConfig',
    'lead.apps.LeadConfig',
    'team.apps.TeamConfig',
]

# middleware-keten, waaronder CORS en standaard beveiliging
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',  # zorg dat CORS headers worden toegevoegd

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# root URL-configuratie en template-instellingen
ROOT_URLCONF = 'veloscrm_django.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'staticfiles'],  # extra map voor statische bestanden
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

# WSGI- en ASGI-entrypoints (ASGI in asgi.py, WSGI hier)
WSGI_APPLICATION = 'veloscrm_django.wsgi.application'

# databaseconfiguratie: SQLite voor eenvoud
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# wachtwoordvalidators voor betere beveiliging
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# internationalisatie en tijdzone
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# statische bestanden (CSS, JS, afbeeldingen)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# standaard veldtype voor automatisch gegenereerde velden
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DRF-configuratie: token-authenticatie en standaard permissie
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}
