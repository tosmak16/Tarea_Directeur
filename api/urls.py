from rest_framework import routers
from .views import TareaViewSet
from django.conf.urls import url, include

router = routers.DefaultRouter()

router.register(r'tareas', TareaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]