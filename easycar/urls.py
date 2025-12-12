from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from users.views import PerfilClienteViewSet, MeusAlugueisView
from users.views import UserViewSet
from cars.views import CarroViewSet
<<<<<<< HEAD
from rentals.views import AlugarViewSet
=======
from django.views.generic import RedirectView
>>>>>>> origin/main


router = routers.DefaultRouter()
router.register(r'carros', CarroViewSet, basename='carro')
router.register(r'users', UserViewSet, basename='user')
<<<<<<< HEAD
router.register(r'clientes', PerfilClienteViewSet, basename='cliente')
router.register(r'alugueis', AlugarViewSet, basename='aluguel')
=======
router.register(r'perfis-clientes', PerfilClienteViewSet, basename='perfil-cliente')
>>>>>>> origin/main

urlpatterns = [
    path('', RedirectView.as_view(url='api/', permanent=False)),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/me/alugueis/', MeusAlugueisView.as_view({'get': 'list'}), name='meus-alugueis'),
]
