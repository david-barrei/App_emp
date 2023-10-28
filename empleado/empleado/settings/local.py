
from .base import *

# Este fichero es para hacer pruebas locales 
DEBUG = True  

ALLOWED_HOSTS = []


DATABASES = { #Configuracion para la base de datos
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
STATIC_URL = 'static/'

