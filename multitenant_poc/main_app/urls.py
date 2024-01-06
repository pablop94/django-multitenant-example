from django.urls import include, path
from rest_framework.routers import DefaultRouter

from main_app.views import DogViewSet

router = DefaultRouter()
router.register(r'dog', DogViewSet)

urlpatterns = [
  path('', include(router.urls)),
]
