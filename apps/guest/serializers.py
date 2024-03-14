from rest_framework.serializers import ModelSerializer
from .models import Guest

class GuestSerializer(ModelSerializer):
    class Meta:
        model = Guest
        fields = ("id", "username", "first_name", "last_name", "email", "password", )
