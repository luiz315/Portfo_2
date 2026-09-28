import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Hosts permitidos na Vercel
ALLOWED_HOSTS = ['.vercel.app', '.now.sh', '127.0.0.1', 'localhost']
# ou libere temporariamente para teste:
# ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # seus outros apps aqui
]
# Application definition - WhiteNoise deve vir logo após SecurityMiddleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # <- ADICIONE AQUI
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Arquivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.parent / 'staticfiles_build' / 'static'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Para Django 4.2+ use STORAGES (recomendado):
# STORAGES = {
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }

# WSGI - Vercel precisa disso
WSGI_APPLICATION = 'seproject.wsgi.application'