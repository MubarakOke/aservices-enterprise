SECRET_KEY= "django-insecure-nmb4c8u$&6$+jo)74#1=ubi$)-42z12!2!w5mam0foqowug&3("
DEBUG= False
PRODUCTION= False
DJANGO_SETTINGS_MODULE= "config.settings.local"
DEFAULT_FILE_STORAGE="cloudinary_storage.storage.MediaCloudinaryStorage"
API_VERSION="v1"
CORS_ALLOWED_ORIGINS=True
DJANGO_PASSWORD_RESET_TOKEN_EXPIRATION_SECS=1800
DJANGO_PASSWORD_RESET_PAGE="http://localhost:3000/reset-password"
CELERY_TIMEZONE="UTC"
CELERY_BROKER="redis://localhost:6379/0"
CELERY_BACKEND="redis://localhost:6379/0"
DJANGO_DEFAULT_FROM_EMAIL="hakeemolajuwon@gmail.com"
EMAIL_HOST_PASSWORD="**************"
EMAIL_HOST="smtp.gmail.com"
EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"