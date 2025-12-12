from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users.views import PerfilClienteViewSet, MeusAlugueisView
from users.views import UserViewSet
from cars.views import CarroViewSet
from django.views.generic import RedirectView
from rentals.views import AlugarViewSet


router = routers.DefaultRouter()
router.register(r'carros', CarroViewSet, basename='carro')
router.register(r'users', UserViewSet, basename='user')
router.register(r'perfis-clientes', PerfilClienteViewSet, basename='perfil-cliente')
router.register(r'clientes', PerfilClienteViewSet, basename='cliente')
router.register(r'alugar', AlugarViewSet, basename='aluguel')

urlpatterns = [
    path('', RedirectView.as_view(url='api/', permanent=False)),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/me/alugueis/', MeusAlugueisView.as_view({'get': 'list'}), name='meus-alugueis'),
]
