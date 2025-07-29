from django.urls import path
from .views import GraciasPorTuPago, ErrorEnElPago


urlpatterns = [
    path('gracias/', GraciasPorTuPago.as_view(), name='gracias'),
    path('error/', ErrorEnElPago.as_view(), name='error_pago'),
]
