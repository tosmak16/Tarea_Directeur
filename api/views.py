# Create your views here.
from rest_framework import viewsets, permissions, mixins
from .models import Tarea
from .serializers import TareaSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .permissions import IsOwner, AdminListPermission


class TareaViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                viewsets.GenericViewSet):

    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = (permissions.IsAuthenticated, AdminListPermission)


class TareaDetailViewSet(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):

    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    lookup_field = 'id'


class UserAuthenticationView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response({'message': 'username and password is incorrect'})
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk, 'email': user.email })


