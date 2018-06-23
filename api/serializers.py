from rest_framework import serializers
from .models import Tarea


class TareaSerializer(serializers.ModelSerializer):

    """Serializer to map model instance into JSON format."""
    class Meta:
        model = Tarea
        fields = ('id', 'title', 'description', 'created_at', 'updated_at',)
        read_only_fields = ('created_at', 'updated_at',)
