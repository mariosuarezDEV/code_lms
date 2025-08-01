from django.urls import path
from .views import LandingPageView, PresalePageView, SponsorView

urlpatterns = [
    path("", LandingPageView.as_view(), name="landing"),
    path("lanzamiento/", PresalePageView.as_view(), name="lanzamiento"),
    path("patrocinadores/", SponsorView.as_view(), name="patrocinadores"),
]
