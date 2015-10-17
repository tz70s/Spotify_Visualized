# import all default settings
from .settings import *
import os

# Static asset configuration
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Turn off DEBUG mode
DEBUG = False

TEMPLATE_DEBUG = False
