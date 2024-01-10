from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("", include("inter_de_la_paz.landing.urls", namespace="landing")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
