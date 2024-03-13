
from django.contrib.auth.models import AbstractUser
from django.db.models import *




class Guest(AbstractUser):
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64)
    phone_number = CharField(max_length=13)
    passport_seria = CharField(max_length=20)

