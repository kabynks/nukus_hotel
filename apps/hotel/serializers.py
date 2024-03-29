from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework.serializers import MultipleChoiceField
class HotelSerializer(ModelSerializer):

    class Meta:
        model = Hotel
        fields = "__all__"

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"