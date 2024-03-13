from django.contrib.admin import *
from .models import *

@register(Hotel)
class HotelAdmin(ModelAdmin):
    list_display = ("id", "name", "address", "city")
    list_display_links = ("id", "name")
    ordering = ("-id",)

@register(Room)
class RoomAdmin(ModelAdmin):
    list_display = ("id", "hotel", "number", "is_used")
    list_display_links = ("id", "number")

@register(Booking)
class BookingAdmin(ModelAdmin):
    list_display = ("id", "room", "guest", "check_in_date", "check_out_date", "is_paid")
    list_display_links = ("id", "room")
