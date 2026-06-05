import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "your-default-secret-key")
DEBUG = os.getenv("DEBUG", "False") == "True"
ALLOWED_HOSTS = os.getenv("https://nagarikbadapatra.com", "127.0.0.1,localhost").split(",")

# settings.py
LOGIN_REDIRECT_URL = '/admin/'  # This will redirect users to the Django admin panel after login


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    'whitenoise.runserver_nostatic',
    "django.contrib.staticfiles",
    "pages",
    "captcha",  # for reCAPTCHA
    'django_recaptcha',

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # MUST be before your middleware
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "pages.middleware.AdminAutoLogoutMiddleware",  # Ensure it's included here
]

SESSION_COOKIE_AGE = 300  # 5 minutes
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True

ROOT_URLCONF = "myproject.urls"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Make sure this includes your templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'pages.context_processors.global_logo',
            ],
        },
    },
]


WSGI_APPLICATION = "myproject.wsgi.application"
    
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


myenv = os.getenv("MY_ENV","prod")
if myenv == "dev":
    DATABASES = {
        "default": {
            # Development: Use SQLite for local development
            "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.sqlite3"),
            "NAME": os.getenv("DB_NAME", BASE_DIR / "db.sqlite3"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DB_NAME", "your_db_name"),
            "USER": os.getenv("DB_USER", "your_db_user"),
            "PASSWORD": os.getenv("DB_PASSWORD", "your_db_password"),
            "HOST": os.getenv("DB_HOST", "postgres-db"),
            "PORT": os.getenv("DB_PORT", "5432"),
        }
    }
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = [
    'https://nagarikbadapatranepal.com',
    'http://localhost:8000',
    'http://nagarikbadapatranepal.com',

]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
INTERNAL_IPS = ['127.0.0.1']

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Google reCAPTCHA Keys
RECAPTCHA_PUBLIC_KEY = os.getenv("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.getenv("RECAPTCHA_PRIVATE_KEY")
SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error']

# SMTP Email Configuration for Password Reset
# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'mail.techprogramming.org'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False  # Make sure this is not True
# EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.techprogramming.org'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'admin@techprogramming.org'
EMAIL_HOST_PASSWORD = 'Prabit@123'  # Your email password here
DEFAULT_FROM_EMAIL = 'admin@techprogramming.org'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DATA_UPLOAD_MAX_MEMORY_SIZE = 524288000  # 500MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 524288000  # 500MB

