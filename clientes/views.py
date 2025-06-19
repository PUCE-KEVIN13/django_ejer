# Importa la función 'render' para devolver plantillas HTML como respuesta,
# y 'redirect' para redirigir al usuario a otra URL
from django.shortcuts import render, redirect

# Importa el modelo Cliente definido en models.py
from .models import Cliente

# -------------------------
# Vista: Página de inicio
# -------------------------
def landing(request):
    # Renderiza y devuelve la plantilla 'landing.html' dentro de la carpeta 'clientes'
    return render(request, 'clientes/landing.html')

# -------------------------
# Vista: Formulario para crear un cliente
# -------------------------
def formulario(request):
    # Si el método de la solicitud es POST (se envió el formulario)
    if request.method == 'POST':
        # Captura los datos enviados desde el formulario HTML (por nombre del input)
        nombre = request.POST.get('nombre')  # obtiene el valor del input 'nombre'
        email = request.POST.get('email')    # obtiene el valor del input 'email'

        # Crea un nuevo objeto Cliente y lo guarda automáticamente en la base de datos
        Cliente.objects.create(nombre=nombre, email=email)

        # Redirige al usuario a la página principal (landing)
        return redirect('/')

    # Si el método no es POST (por ejemplo, GET), muestra el formulario vacío
    return render(request, 'clientes/formulario.html')  # OJO: aquí dice 'cliente', debería ser 'clientes' si sigues la convención del resto

# -------------------------
# Vista: Listado de clientes registrados
# -------------------------
def listado(request):
    # Recupera todos los objetos Cliente desde la base de datos
    clientes = Cliente.objects.all()

    # Renderiza la plantilla 'listado.html' pasando el contexto con los clientes
    return render(request, 'clientes/listado.html', {'clientes': clientes})

# Create your views here.
