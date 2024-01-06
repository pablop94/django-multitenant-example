from multitenant_poc.middleware import get_current_db_name


class TenantDatabaseRouter:
  def db_for_read(self, model, **hints):
    return get_current_db_name()

  def db_for_write(self, model, **hints):
    return get_current_db_name()