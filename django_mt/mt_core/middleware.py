import django
import logging
from django.conf import settings
from django import setup
from .utils import get_tenant
from django.db import connection

if django.VERSION >= (1, 11, 0):
    MIDDLEWARE_MIXIN = django.utils.deprecation.MiddlewareMixin
else:
    MIDDLEWARE_MIXIN = object

LOGGER = logging.getLogger('django_mt')


class MTMiddleware(MIDDLEWARE_MIXIN):

    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        # get hostname
        hostname = request.get_host().split(':')[0].lower()
        LOGGER.info('hostname: %s' % (hostname))

        default_db_info = settings.DATABASES['default']

        # get tenant db_info - just put these tables in cacheops, we dont need to deal with redis explicitly
        db_info = get_tenant(hostname)

        # set db cursor via the database wrapper
        connection.db_info = db_info
