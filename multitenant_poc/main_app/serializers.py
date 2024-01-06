from rest_framework.serializers import ModelSerializer

from main_app.models import Perro


class PerroSerializer(ModelSerializer):
  class Meta:
    model = Perro
    fields = '__all__'