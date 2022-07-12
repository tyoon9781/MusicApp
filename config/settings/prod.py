from config.settings._base import *

DEBUG = False

ALLOWED_HOSTS = ["3.39.222.238", "qbicpiano.com"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "musicdatabase",
        'USER': "tyoon9781",
        "PASSWORD": "Qmfkdlepdl3#",
        "HOST": "database-musicdb.cqqllafleflh.ap-northeast-2.rds.amazonaws.com",
        "PORT": "5432",
    }
}