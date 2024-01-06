import threading
from django.db import connections

THREAD_LOCAL = threading.local()

class TenantMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response

  def __call__(self, request):
    db = request.META.get('SERVER_NAME').split('.')[0]
    setattr(THREAD_LOCAL, "DB", db)
    response = self.get_response(request)
    return response


def get_current_db_name():
  return getattr(THREAD_LOCAL, "DB", None)