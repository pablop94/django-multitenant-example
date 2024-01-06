# Django multitenant

## Configuración Django

### Bases de datos
Tenemos 2 bases de datos de postgres que las configuramos con docker-compose.
```bash
docker-compose up
```

#### Settings
En `multitenant_poc.settings.py` configuramos `DATABASES`:
```python
DATABASES = {
    'default': {},
    "client1": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "client1",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "127.0.0.1",
        "PORT": "15432",
    },
    "client2": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "client2",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "127.0.0.1",
        "PORT": "25432",
    }
}
```

### Middleware
Configuramos un middleware que se encarga de definir la bd a usar según el cliente: `multitenant_poc.middleware.TenantMiddleware`, donde obtenemos y seteamos la db según el `SERVER_NAME`. Esta variable se setea desde `mod_wsgi`.
```python
    db = request.META.get('SERVER_NAME').split('.')[0]
    setattr(THREAD_LOCAL, "DB", db)
```
*`THREAD_LOCAL` es la variable que usamos para mantener los datos del thread.*

#### Settings
En `multitenant_poc.settings.py` configuramos `MIDDLEWARE`
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'multitenant_poc.middleware.TenantMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

### Router
Para que django sepa manejar distintas bases de datos, tenemos que usar un Router, para eso creamos `multitenant_poc.router.TenantDatabaseRouter`:

```python
from multitenant_poc.middleware import get_current_db_name


class TenantDatabaseRouter:
  def db_for_read(self, model, **hints):
    return get_current_db_name()

  def db_for_write(self, model, **hints):
    return get_current_db_name()
```
Donde `get_current_db_name` se define como:

```python
def get_current_db_name():
  return getattr(THREAD_LOCAL, "DB", None)
```
Usando `THREAD_LOCAL`.

#### Settings
En `multitenant_poc.settings.py` configuramos `DATABASE_ROUTERS`

```python
DATABASE_ROUTERS = ['multitenant_poc.router.TenantDatabaseRouter']
```

## Configuración Apache
Se crearon 2 archivos de configuración, uno para cada cliente, `client1.conf` y `client2.conf`, ubicados en `apache/sites-available/`.
En esos archivos se configura mod_wsgi para que apunte a `multitenant_poc.wsgi.py`.

**Importante** Se debe configurar `WSGIApplicationGroup %{GLOBAL}` para evitar problemas al cargar psycopg2, ya que si no se configura así, nos da error porque psycopg2 se puede cargar 1 vez por intérprete de python.

A modo de ejemplo dejo la configuración de mpm-event en `apache/conf-available/`


## Fuente
[Building Multi Tenant Applications with
Django Documentation](https://readthedocs.org/projects/building-multi-tenant-applications-with-django/downloads/pdf/latest/)