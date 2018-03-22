from metanic.settings.development import *

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
            'NAME': 'metanic',
            'USER': 'MetanicUser',
            'PASSWORD': 'MetanicDevelopment',
            'HOST': 'postgres',
            'PORT': '5432',
        }
}
