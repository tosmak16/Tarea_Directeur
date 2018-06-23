from rest_framework import routers
from .views import TareaViewSet, UserAuthenticationView, TareaDetailViewSet
from django.conf.urls import url, include

router = routers.DefaultRouter()

router.register(r'tareas', TareaViewSet)
router.register(r'tareas', TareaDetailViewSet)

urlpatterns = [
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^users/signin/', UserAuthenticationView.as_view())

]