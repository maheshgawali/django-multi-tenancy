import logging
from django_mt.mt_core.models import DomainDb, DbDetails

LOGGER = logging.getLogger('django_mt')


def get_tenant(hostname):
    domain_db = DomainDb.objects.using('default').get(name=hostname)
    db_obj = DbDetails.objects.using('default').get(id=domain_db.db_id)
    # LOGGER.info('domain_db: %s, db_obj: %s', domain_db, db_obj)
    return db_obj
