from instances import ENV_VAR
import os, json
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = ENV_VAR['CSRF_KEY']
#web address:
SITE_ROOT = ENV_VAR['SITE_ROOT']
#Propagate exceptions:
PROPAGATE_EXCEPTIONS = True

