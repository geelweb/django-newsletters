
INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'widget_tweaks',
    'geelweb.django.twitter_bootstrap_form',
    'geelweb.django.newsletters',
)

SECRET_KEY = '$-muc7nzd^9g9z^f+^8@^inpbpixz=)d8k%g%qsgrw*3+)^1t_'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

STATIC_URL = '/static/'

ROOT_URLCONF = 'tests.urls'
