from django.urls import path
from .views import GraciasPorTuPago, ErrorEnElPago, AccesoAnticipadoView


urlpatterns = [
    path(
        "acceso-anticipado/<int:id>/",
        AccesoAnticipadoView.as_view(),
        name="acceso_anticipado",
    ),
    path("gracias/", GraciasPorTuPago.as_view(), name="gracias"),
    path("error/", ErrorEnElPago.as_view(), name="error_pago"),
]
