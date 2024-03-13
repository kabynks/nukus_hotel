from django.urls import path
from .views import *

urlpatterns = [
    path("", homepage, name="home"),
    path("hotels/", Hotels_List.as_view(), name="hotels_list"),
    path("hotels/<int:pk>/", Hotel_Detail.as_view(), name="hotel_detail"),
    path("hotels/<int:pk>/rooms/", hotel_rooms, name="hotel_rooms")
]