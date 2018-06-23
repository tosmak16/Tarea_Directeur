# Create your views here.
from rest_framework import viewsets
from .models import Tarea
from .serializers import TareaSerializer


class TareaViewSet(viewsets.ModelViewSet):

    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    lookup_field = 'id'
