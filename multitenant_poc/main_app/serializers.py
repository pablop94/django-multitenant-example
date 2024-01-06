from rest_framework.serializers import ModelSerializer

from main_app.models import Dog


class DogSerializer(ModelSerializer):
  class Meta:
    model = Dog
    fields = '__all__'