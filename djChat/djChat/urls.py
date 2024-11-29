from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
     # YOUR PATTERNS
    path('api/docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    # # Optional UI:
    path('api/docs/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
