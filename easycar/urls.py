from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users.views import PerfilClienteViewSet
from users.views import UserViewSet
from cars.views import CarroViewSet
from django.views.generic import RedirectView


router = routers.DefaultRouter()
router.register(r'carros', CarroViewSet, basename='carro')
router.register(r'users', UserViewSet, basename='user')
router.register(r'clientes', PerfilClienteViewSet, basename='cliente')

urlpatterns = [
    path('', RedirectView.as_view(url='api/', permanent=False)),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
