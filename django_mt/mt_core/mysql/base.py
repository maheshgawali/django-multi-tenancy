from importlib import import_module
import logging
import time

from django.core.exceptions import ImproperlyConfigured

import django.db.backends.mysql.base
WRAPPED_BACKEND = import_module('django.db.backends.mysql.base')

LOGGER = logging.getLogger('db_multitenant')


class DatabaseWrapper(WRAPPED_BACKEND.DatabaseWrapper):

    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)
        self.db_info = None
        self.default_db_info = None

    def _cursor(self):
        cursor = super(DatabaseWrapper, self)._cursor()

        # create a new db object here and set it to connection and db_name
        if self.db_info:
            print('db_info: %s' % (self.db_info))

        # now init the connection using data from db_info and set it to cursor
        # connection = cursor.cursor.connection

        conn_params = {
            'ENGINE': self.db_info.engine,
            'NAME': self.db_info.name,
            'USER': self.db_info.user,
            'PASSWORD': self.db_info.password,
            'HOST': self.db_info.host,
            'PORT': self.db_info.port,
            'OPTIONS': self.db_info.options
        }

        connection = cursor.get_new_connection(self, conn_params)
        LOGGER.info('connection: %s', connection.__dict__)
        LOGGER.info('cursor.cursor.connection: %s',
                    cursor.cursor.connection.__dict__)
        cursor.cursor.connection = connection

        # connection_db_name = getattr(connection, 'mt_db_name', None)

        # if connection_db_name != db_name:
        #     start_time = time.time()
        #     cursor.execute('USE `%s`;' % db_name)
        #     time_ms = int((time.time() - start_time) * 1000)
        #     LOGGER.debug('Applied db_name `%s` in %s ms', db_name, time_ms)
        #     connection.mt_db_name = db_name

        return cursor
