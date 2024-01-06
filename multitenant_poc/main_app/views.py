from rest_framework.viewsets import ModelViewSet

from main_app.serializers import PerroSerializer
from main_app.models import Perro


class PerroViewSet(ModelViewSet):
  queryset = Perro.objects.all()
  serializer_class = PerroSerializer
