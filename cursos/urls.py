from django.urls import path
from .views import CursoDetailView


urlpatterns = [
    path('detalle/<int:pk>/', CursoDetailView.as_view(), name='curso_detalle'),
]
