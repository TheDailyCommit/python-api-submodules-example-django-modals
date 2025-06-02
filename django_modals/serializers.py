from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer for the Todo model.
    """

    class Meta:
        model = Todo
        fields = ["id", "title", "description", "completed", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]
