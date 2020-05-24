from .settings import *

with open('/etc/config.json') as config_file:
    config = json.load(config_file)

DEBUG = False

CORS_ORIGIN_ALLOW_ALL = False

