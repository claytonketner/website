# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
from .key import SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
from .secret import DEBUG
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['localhost', '.claytonketner.com']

from .secret import HOST


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'adminfiles',
    'django_extensions',
    'markdown_deux',
    'pagedown',
    'sorl.thumbnail',

    'blog',
    'my_adminfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'portfolio.urls'

WSGI_APPLICATION = 'portfolio.wsgi.application'

from .secret import BASE_PATH
from .secret import BASE_WEB_PATH
STATIC_URL = '/portfolio/static/'
STATIC_ROOT = BASE_WEB_PATH + 'portfolio/static/'
STATICFILES_DIRS = (
    BASE_PATH + 'portfolio/site_media/',
    BASE_PATH + 'portfolio/site_media/uploads/',
)
TEMPLATE_DIRS = (
    BASE_PATH + 'portfolio/templates/',
)

# Database
from .secret import DB_ENGINE
from .secret import DB_NAME
from .secret import DB_USER
from .secret import DB_PASS
from .secret import DB_HOST

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': DB_HOST,
        'PORT': '3306',
    }
}

SHELL_PLUS = 'ipython'
ADMINFILES_UPLOAD_TO = 'portfolio/site_media/uploads/'
THUMBNAIL_EXTENSION = 'png'
MARKDOWN_DEUX_STYLES = {
    "default": {
        "extras": { "code-friendly": None, },
        "safe_mode": "escape",
    },
    "trusted": {
        "extras": { "code-friendly": None, },
        "safe_mode": False,
    }
}

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
