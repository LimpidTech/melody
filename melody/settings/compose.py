from melody.settings.development import *

CACHES = {
    'default':
        {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': 'memcached:11211',
        }
}

DATABASES = {
    'default':
        {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'melody',
            'USER': 'MelodyUser',
            'PASSWORD': 'MelodyDevelopment',
            'HOST': 'postgres',
            'PORT': '5432',
        }
}
