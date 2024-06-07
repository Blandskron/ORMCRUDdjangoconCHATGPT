from django.urls import path
from .views import *

urlpatterns = [
    # Home
    path('', home, name='home'),
    # CONSULTA PERSONALIZADA
    path('consulta/', consulta_personalizada, name='consulta_personalizada'),
    # AUTOR
    path('autores/', AutorListView.as_view(), name='autor_list'),
    path('autores/<int:pk>/', AutorDetailView.as_view(), name='autor_detail'),
    path('autores/crear/', AutorCreateView.as_view(), name='autor_create'),
    path('autores/<int:pk>/actualizar/', AutorUpdateView.as_view(), name='autor_update'),
    path('autores/<int:pk>/borrar/', AutorDeleteView.as_view(), name='autor_delete'),
    path('autor/<int:pk>/eliminar/', confirm_delete_autor, name='confirm_delete_autor'),   
    # LIBRO
    path('libros/', LibroListView.as_view(), name='libro_list'),
    path('<int:pk>/', LibroDetailView.as_view(), name='libro_detail'),
    path('crear/', LibroCreateView.as_view(), name='libro_create'),
    path('<int:pk>/actualizar/', LibroUpdateView.as_view(), name='libro_update'),
    path('<int:pk>/borrar/', LibroDeleteView.as_view(), name='libro_delete'),
    path('libros/<int:pk>/eliminar/', confirm_delete_libro, name='confirm_delete_libro'),   
]
