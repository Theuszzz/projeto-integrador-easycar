from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users.views import PerfilClienteViewSet

router = routers.DefaultRouter()
router.register(r'clientes', PerfilClienteViewSet, basename='cliente')

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
