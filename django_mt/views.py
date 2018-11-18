from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
import logging

# from django.db import connection

LOGGER = logging.getLogger('django_mt')


# @login_required
def loginView(request):
    # return HttpResponse('%s' % request.__dict__)
    # LOGGER.info('connection.settings_dict: %s', connection.settings_dict)
    usr = get_user_model().objects.filter().first()
    LOGGER.info('get_user_model().objects.all().first(): %s', usr)
    # print(connection.queries)
    return HttpResponse('%s' % (usr if usr else 'Hello, World!'))
