from django.urls import include, path
from rest_framework.routers import DefaultRouter

from main_app.views import PerroViewSet

router = DefaultRouter()
router.register(r'perro', PerroViewSet)

urlpatterns = [
  path('', include(router.urls)),
]
