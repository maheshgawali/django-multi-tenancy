from importlib import import_module
import logging
import time
import json
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
import django.db.backends.mysql.base
WRAPPED_BACKEND = import_module('django.db.backends.mysql.base')

LOGGER = logging.getLogger('django_mt')


def lower_dict(d):
    new_dict = dict((k.lower(), v) for k, v in d.items())
    return new_dict


class DatabaseWrapper(WRAPPED_BACKEND.DatabaseWrapper):

    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)
        self.db_info = None
        # self.default_db_info = None
        self.default_db_info = settings.DATABASES['default']

    def _cursor(self):
        cursor = super(DatabaseWrapper, self)._cursor()

        # create a new db object here and set it to connection and db_name
        # LOGGER.info('if db_info: %s' % (self.db_info))
        # LOGGER.info('if default_db_info: %s' % (self.default_db_info))
        conn_params = None
        if self.db_info:
            # LOGGER.info('db_info: %s', self.db_info.__dict__)
            LOGGER.info('--- using %s db connection ---', self.db_info.name)
            # now init the connection using data from db_info and set it to cursor
            # connection = cursor.cursor.connection

            conn_params = {
                'ENGINE': self.db_info.engine,
                'NAME': self.db_info.name,
                'USER': self.db_info.user,
                'PASSWORD': self.db_info.password,
                'HOST': self.db_info.host,
                'PORT': self.db_info.port,
                # 'OPTIONS': json.loads(self.db_info.options)
                'OPTIONS': {},
                'AUTOCOMMIT': False
            }
            # LOGGER.info('BEFORE conn_params: %s', conn_params)
            self.settings_dict = conn_params
            updated_conn_params = self.get_connection_params()
            # LOGGER.info('AFTER updated_conn_params: %s', updated_conn_params)

            # LOGGER.info('BEFORE cursor.cursor.connection: %s',
            #             cursor.cursor.connection.__dict__)

            connection = self.get_new_connection(updated_conn_params)
            # self.connection = connection

            return connection.cursor()
        else:
            LOGGER.info('--- using default db connection ---')
            return cursor
