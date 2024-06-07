from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Libro, Autor
from django.shortcuts import render, get_object_or_404
from django.db import connection


def home(request):
    return render(request, 'crudorm/home.html')

# TIPOS DE CONSULTAS
# SELECT nombre, bio FROM crudorm_autor;
# SELECT a.nombre AS autor, l.titulo AS libro, l.publicacion FROM crudorm_autor AS a JOIN crudorm_libro AS l ON a.id = l.autor_id;
# SELECT titulo AS crudorm_libro, publicacion FROM crudorm_libro WHERE publicacion < '1980-01-01';
# CONSULTAS SQL
def consulta_personalizada(request):
    # Realizar la consulta SQL
    with connection.cursor() as cursor:
        cursor.execute("SELECT titulo AS crudorm_libro, publicacion FROM crudorm_libro WHERE publicacion < '1980-01-01';")
        rows = cursor.fetchall()

    # Renderizar la plantilla con los resultados de la consulta
    return render(request, 'crudorm/resultado_consulta.html', {'rows': rows})

# READ
class AutorListView(ListView):
    model = Autor
    template_name = 'crudorm/autor_list.html'

# READ
class AutorDetailView(DetailView):
    model = Autor
    template_name = 'crudorm/autor_detail.html'

# CREAD
class AutorCreateView(CreateView):
    model = Autor
    template_name = 'crudorm/autor_form.html'
    fields = ['nombre', 'bio']
    success_url = reverse_lazy('autor_list')

# UPDATE
class AutorUpdateView(UpdateView):
    model = Autor
    template_name = 'crudorm/autor_form.html'
    fields = ['nombre', 'bio']
    success_url = reverse_lazy('autor_list')

def confirm_delete_autor(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'crudorm/autor_confirm_delete.html', {'object': libro})


# DELETE
class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'crudorm/autor_confirm_delete.html'
    success_url = reverse_lazy('autor_list')

# READ
class LibroListView(ListView):
    model = Libro
    template_name = 'crudorm/libro_list.html'

# READ
class LibroDetailView(DetailView):
    model = Libro
    template_name = 'crudorm/libro_detail.html'

# CREATE
class LibroCreateView(CreateView):
    model = Libro
    template_name = 'crudorm/libro_form.html'
    fields = ['titulo', 'autor', 'publicacion']
    success_url = reverse_lazy('libro_list')

# UPDATE
class LibroUpdateView(UpdateView):
    model = Libro
    template_name = 'crudorm/libro_form.html'
    fields = ['titulo', 'autor', 'publicacion']
    success_url = reverse_lazy('libro_list')

def confirm_delete_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'crudorm/libro_confirm_delete.html', {'object': libro})

# DELETE
class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'crudorm/libro_confirm_delete.html'
    success_url = reverse_lazy('libro_list')
