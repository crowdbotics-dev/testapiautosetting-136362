from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors136362ViewSet

router = DefaultRouter()
router.register(
    "testconnectors136362", Testconnectors136362ViewSet, basename="testconnectors136362"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
