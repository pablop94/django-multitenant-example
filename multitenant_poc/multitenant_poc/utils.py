import random

def tenant_db_from_request(request):
  # client.local
  return request.META.get('SERVER_NAME').split('.')[0]