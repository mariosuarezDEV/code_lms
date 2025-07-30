from django.urls import path
from .views import ProfileView, UpdateProfileView

urlpatterns = [
    path("", ProfileView.as_view(), name="account_profile"),
    path("update/", UpdateProfileView.as_view(), name="account_update_profile"),
]
