from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
import logging

from django.db import connection
from django.db import connections

LOGGER = logging.getLogger('django_mt')


# @login_required
def loginView(request):
    # return HttpResponse('%s' % request.__dict__)
    LOGGER.info('connection.settings_dict: %s', connection.settings_dict)
    LOGGER.info('connections._databases: %s', connections._databases)
    LOGGER.info('get_user_model().objects.all(): %s',
                get_user_model().objects.all())
    return HttpResponse('Hello, World!')
