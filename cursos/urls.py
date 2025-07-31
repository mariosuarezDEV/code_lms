from django.urls import path
from .views import CursoDetailView, CursoListView


urlpatterns = [
    path("", CursoListView.as_view(), name="curso_lista"),
    path("detalle/<int:pk>/", CursoDetailView.as_view(), name="curso_detalle"),
]
