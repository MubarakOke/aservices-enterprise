import os
from pathlib import Path

import environ
from celery import Celery
from config.literals import DJANGO_SETTINGS_MODULE

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
env = environ.Env()
# Fetching
env_dir = os.path.join(ROOT_DIR, "envs", ".env")
if os.path.exists(env_dir):
    environ.Env.read_env(env_dir)
# setting the Django settings module.
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", env.str("DJANGO_SETTINGS_MODULE", DJANGO_SETTINGS_MODULE)
)
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
# Looks up for task modules in Django applications and loads them
app.autodiscover_tasks()
