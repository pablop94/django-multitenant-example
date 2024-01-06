from rest_framework.viewsets import ModelViewSet

from main_app.serializers import DogSerializer
from main_app.models import Dog


class DogViewSet(ModelViewSet):
  queryset = Dog.objects.all()
  serializer_class = DogSerializer
