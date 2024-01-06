import random

def tenant_db_from_request(request):
  return random.choice(['client1', 'client2'])