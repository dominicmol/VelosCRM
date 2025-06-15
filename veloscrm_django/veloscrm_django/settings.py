from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wn_v7z89$xlu+@uyo@um7_0mzlbcc_m$i$6x5+(#tx)3j%%auy'

# Stripe
STRIPE_PUB_KEY = 'pk_test_51IskUtBa5bOHd7L5NTRJPnQa7bKWKhKzTQwGqDQ1IU2PnCK78kHqAoHQcP4iFjpTL2SoSk5miaLTL4LjYf1nE72k00UvoOvrnA'
STRIPE_SECRET_KEY = 'sk_test_51IskUtBa5bOHd7L5JLISWCnXcFxecSIZdUQfcXBbJAj3NpqfRrR4gDrBulRMjiGF64oPk7RGCboqKI71q7ATN5n800THD65kE0'
STRIPE_PRICE_ID_SMALL_TEAM = 'price_1IuXkUBa5bOHd7L5VxwI8XnS'
STRIPE_PRICE_ID_BIG_TEAM = 'price_1IuXlABa5bOHd7L5D7zel5a6'
STRIPE_WEBHOOK_KEY = 'whsec_iV0qP1UMZEvR53tkDW7rGBE6EgFZ6sxj'

FRONTEND_WEBSITE_SUCCESS_URL = 'http://localhost:8081/dashboard/team/plans/thankyou'
FRONTEND_WEBSITE_CANCEL_URL = 'http://localhost:8081/dashboard/team/plans'

DEBUG = True
ALLOWED_HOSTS = []

# ✅ CORS fix: voeg alle nodige origins toe
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8080',
    'http://localhost:8081',
    'http://localhost:8082',  
]

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

# Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'djoser',
    'client.apps.ClientConfig',
    'lead.apps.LeadConfig',
    'team.apps.TeamConfig',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # <== moet voor CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'veloscrm_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'veloscrm_django.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Language & time
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'

# Default primary key field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
