from rest_framework import routers
from .views import TareaViewSet, UserAuthenticationView
from django.conf.urls import url, include

router = routers.DefaultRouter()

router.register(r'tareas', TareaViewSet)

urlpatterns = [
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^users/signin/', UserAuthenticationView.as_view())
]