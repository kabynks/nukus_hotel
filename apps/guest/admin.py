

from django.contrib.admin import *
from .models import Guest

@register(Guest)
class GuestAdmin(ModelAdmin):
    list_display = ("id","first_name", "last_name", "email", "phone_number")
    list_display_links = ("id","first_name", "last_name","email")
    ordering = ("-id",)
    fields = ("first_name", "last_name", "email", "phone_number", "password")