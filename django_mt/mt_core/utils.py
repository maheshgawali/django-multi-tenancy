from django_mt.mt_core.models import DomainDb, DbDetails


def get_tenant(hostname):
    domain_db = DomainDb.objects.get(name=hostname)
    db_obj = DbDetails.objects.get(id=domain_db.db_id)
    return db_obj
