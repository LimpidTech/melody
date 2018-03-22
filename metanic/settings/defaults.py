import os


def env_value(name, default=None):
    name = name.upper()
    return os.environ.get(f'METANIC_{name}', os.environ.get(name, default))


def project_path(*paths):
    return os.path.join(os.getcwd(), *paths)


DATE_FORMAT = 'Y-m-d'
DEFAULT_FROM_EMAIL = 'services@metanic.monokro.me'
EMAIL_BACKEND = 'anymail.backends.mailgun.EmailBackend'
MAILGUN_API_KEY = env_value('mailgun_api_key')
USE_L10N = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'anymail',
    'channels',
    'rest_framework',
    'metanic.accounts',
    'metanic.collector',
    'metanic.core',
    'metanic.mail',
    'metanic.posts',
    'metanic.realtime',
]

MIDDLEWARE = [
    'metanic.core.middleware.CORSMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'metanic.core.middleware.CORSMiddleware',
    'metanic.core.middleware.HeaderExtensionMiddleware',
]

TEMPLATES = [
    {
        'APP_DIRS': True,
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS':
            {
                'context_processors':
                    [
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                        'metanic.core.context_processors.frontend_url',
                    ],
            }
    },
]

CHANNEL_LAYERS = {
    'default':
        {
            'BACKEND': 'asgiref.inmemory.ChannelLayer',
            'ROUTING': 'metanic.realtime.routing.routes',
        }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':
        ['rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'],
}

ANYMAIL = {
    'MAILGUN_API_KEY': MAILGUN_API_KEY,
    'MAILGUN_SENDER_DOMAIN': 'metanic.local',
}

COLLECTION_SERIALIZER_TYPES = {
    'post': ('metanic.posts.api.serializers', 'PostSerializer'),
}

CORS_ALLOWED_HEADERS = [
    'Accept',
    'Content-Type',
    'Authorization',
]

ALLOWED_HOSTS = [
    'localhost',
    'metanic.ngrok.io',
]
