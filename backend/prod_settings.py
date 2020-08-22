import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('db_name'),
        'USER': os.getenv('user_name_db'),
        'PASSWORD': os.getenv('password_db'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# STATIC_DIR = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
