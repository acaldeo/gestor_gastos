from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('gastos.urls')),           # Tu API
    path('auth/', include('dj_rest_auth.urls')),    # Login, logout, password reset
    path('auth/registration/', include('dj_rest_auth.registration.urls')),  # Registro
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)