import os

configuration = os.environ.get('LOCUST_CONFIGURATION', None)

if configuration == 'development':
    from .development import *
elif configuration == 'production':
    from .production import *
else:
    from .base import *
