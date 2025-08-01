from django.urls import path
from .views import (
    GraciasPorTuPago,
    ErrorEnElPago,
    AccesoAnticipadoView,
    SponsorPagoView,
)


urlpatterns = [
    path(
        "acceso-anticipado/<int:id>/",
        AccesoAnticipadoView.as_view(),
        name="acceso_anticipado",
    ),
    path(
        "pago-sponsor/<int:id>/",
        SponsorPagoView.as_view(),
        name="pago_sponsor",
    ),
    # URLs para las vistas de éxito y error de pago
    path("gracias/", GraciasPorTuPago.as_view(), name="gracias"),
    path("error/", ErrorEnElPago.as_view(), name="error_pago"),
]
