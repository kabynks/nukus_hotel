from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from .views import GuestViewSet

router = DefaultRouter()
router.register("api", GuestViewSet, basename="api")

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("logout/", logout_view, name="logout_view"),
    path("login/admin/", login_with_admin, name="login_with_admin")
]
urlpatterns += router.urls