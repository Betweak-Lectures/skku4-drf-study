from .common import *

SECRET_KEY = "kasdflkdsfkcxvcxzmvweporkqwqdslfklkvcxlzvclkowe"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "NAME": "drf_study",
        "USER": "root",
        "PASSWORD": "admin1234"
    }
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


INSTALLED_APPS += [
    
]