from django.contrib import admin
from django.urls import path
from server import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

router = DefaultRouter()
router.register("api/server/select", views.ServerListViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    # YOUR PATTERNS
    path("api/docs/schema/", SpectacularAPIView.as_view(), name="schema"),
    # # Optional UI:
    path(
        "api/docs/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/docs/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
] + router.urls


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
