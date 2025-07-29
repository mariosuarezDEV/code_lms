from django.urls import path
from .views import AccesoAnticipadoView


urlpatterns = [
    path('acceso-anticipado/<int:id>/', AccesoAnticipadoView.as_view(),
         name='acceso_anticipado'),
]
