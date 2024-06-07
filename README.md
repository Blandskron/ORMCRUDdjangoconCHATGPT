### Proyecto Django: Gestión de Autores y Libros

Este proyecto Django permite la gestión de autores y libros. A lo largo de este proyecto, hemos realizado las siguientes tareas:

1. **Configuración del Proyecto Django**
   - Creación del proyecto y la aplicación Django.
   - Configuración de las rutas y vistas iniciales.
   - Configuración de los templates.

2. **Modelos**
   - Creación de los modelos `Autor` y `Libro`.
   - Definición de relaciones y atributos para los modelos.
   - Migraciones para aplicar los cambios a la base de datos.

3. **Vistas y Templates**
   - Creación de vistas genéricas para CRUD de autores y libros (`CreateView`, `UpdateView`, `DetailView`, `DeleteView`, `ListView`).
   - Configuración de templates para cada vista.
   - Integración de Bootstrap para estilos consistentes y responsivos.

4. **Consultas SQL**
   - Implementación de consultas SQL personalizadas para extraer datos específicos de la base de datos.
   - Renderización de resultados de consultas SQL en templates.

5. **Confirmación de Eliminación**
   - Implementación de una vista y un template específicos para confirmar la eliminación de un libro.
   - Ajuste de las URLs para incluir la confirmación de eliminación.

6. **Templates Base y Herencia**
   - Creación de `base.html` como template base.
   - Uso de herencia de templates para extender `base.html` en otros templates.
   - Inclusión de `header.html` y `footer.html` en el template base utilizando Bootstrap.

### Estructura de Directorios

```
consultas/
│
├── consultas/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── crudorm/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── header.html
│   │   ├── footer.html
│   │   ├── autor_confirm_delete.html
│   │   ├── autor_detail.html
│   │   ├── autor_form.html
│   │   ├── autor_list.html
│   │   ├── libro_confirm_delete.html
│   │   ├── libro_detail.html
│   │   ├── libro_form.html
│   │   ├── libro_list.html
│   │   ├── confirm_delete_libro.html
│   │   └── home.html
│   └── tests.py
│
├── manage.py
└── db.sqlite3
```

### Ejemplos de Código

#### URLs

```python
from django.urls import path
from .views import AutorCreateView, AutorUpdateView, AutorDetailView, AutorDeleteView, AutorListView, LibroDetailView, LibroUpdateView, LibroDeleteView, LibroListView, confirm_delete_libro, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('autores/', AutorListView.as_view(), name='autor_list'),
    path('autores/crear/', AutorCreateView.as_view(), name='autor_create'),
    path('autores/<int:pk>/', AutorDetailView.as_view(), name='autor_detail'),
    path('autores/<int:pk>/editar/', AutorUpdateView.as_view(), name='autor_update'),
    path('autores/<int:pk>/eliminar/', AutorDeleteView.as_view(), name='autor_delete'),
    path('libros/', LibroListView.as_view(), name='libro_list'),
    path('libros/<int:pk>/', LibroDetailView.as_view(), name='libro_detail'),
    path('libros/<int:pk>/editar/', LibroUpdateView.as_view(), name='libro_update'),
    path('libros/<int:pk>/eliminar/', confirm_delete_libro, name='confirm_delete_libro'),
    path('libros/<int:pk>/eliminar/confirmar/', LibroDeleteView.as_view(), name='libro_delete'),
]
```

#### Vistas

```python
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from .models import Autor, Libro

class AutorCreateView(CreateView):
    model = Autor
    fields = ['nombre', 'bio']
    template_name = 'autor_form.html'
    success_url = reverse_lazy('autor_list')

class AutorUpdateView(UpdateView):
    model = Autor
    fields = ['nombre', 'bio']
    template_name = 'autor_form.html'
    success_url = reverse_lazy('autor_list')

class AutorDetailView(DetailView):
    model = Autor
    template_name = 'autor_detail.html'

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'autor_confirm_delete.html'
    success_url = reverse_lazy('autor_list')

class AutorListView(ListView):
    model = Autor
    template_name = 'autor_list.html'

class LibroDetailView(DetailView):
    model = Libro
    template_name = 'libro_detail.html'

class LibroUpdateView(UpdateView):
    model = Libro
    fields = ['titulo', 'autor', 'publicacion']
    template_name = 'libro_form.html'
    success_url = reverse_lazy('libro_list')

def confirm_delete_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'confirm_delete_libro.html', {'object': libro})

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'libro_confirm_delete.html'
    success_url = reverse_lazy('libro_list')

class LibroListView(ListView):
    model = Libro
    template_name = 'libro_list.html'

def home_view(request):
    return render(request, 'home.html')
```

#### Templates

- **base.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Django Project{% endblock %}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    {% include 'header.html' %}
    <main class="container mt-4">
        {% block content %}{% endblock %}
    </main>
    {% include 'footer.html' %}
</body>
</html>
```

- **header.html**
```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="{% url 'home' %}">My Django Project</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
            <li class="nav-item">
                <a class="nav-link" href="{% url 'autor_list' %}">Autores</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="{% url 'libro_list' %}">Libros</a>
            </li>
        </ul>
    </div>
</nav>
```

- **footer.html**
```html
<footer class="footer mt-auto py-3 bg-light">
    <div class="container">
        <span class="text-muted">&copy; 2024 My Django Project</span>
    </div>
</footer>
```

- **confirm_delete_libro.html**
```html
{% extends 'base.html' %}

{% block title %}Confirmar Eliminación{% endblock %}

{% block content %}
<div class="container mt-5">
    <h1 class="text-danger">¿Estás seguro de que quieres eliminar "{{ object }}"?</h1>
    <form action="{% url 'libro_delete' object.pk %}" method="post">
        {% csrf_token %}
        <div class="form-group">
            <input type="submit" value="Sí, eliminar" class="btn btn-danger">
            <a href="{% url 'libro_detail' object.pk %}" class="btn btn-secondary">Cancelar</a>
        </div>
    </form>
</div>
{% endblock %}
```

Con estas configuraciones y ajustes, el proyecto ahora permite una gestión efectiva de autores y libros, asegurando una interfaz amigable y estilizada gracias a Bootstrap.