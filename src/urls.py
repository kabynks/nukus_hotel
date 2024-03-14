
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.hotel.urls")),
    path("guest/", include("apps.guest.urls")),
    path('api/auth/', include('dj_rest_auth.urls')),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger/", SpectacularSwaggerView.as_view(), name="swagger"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(), name="redoc"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
