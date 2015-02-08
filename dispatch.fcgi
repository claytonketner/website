#!/home/clayton4/website/.virtualenv/bin/python

import os
import sys

from portfolio.settings.secret import BASE_PATH


sys.path.insert(0, BASE_PATH + '.virtualenv/lib/python2.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio.settings.base'

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
