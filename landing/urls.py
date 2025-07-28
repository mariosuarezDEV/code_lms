from django.urls import path
from .views import LandingPageView, PresalePageView
urlpatterns = [
    path("", LandingPageView.as_view(), name="landing"),
    path("lanzamiento/", PresalePageView.as_view(), name="lanzamiento")
]
