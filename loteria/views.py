from django.shortcuts import render, redirect
from .forms import RegistroLoteriaForm  # Importamos el formulario (lo creamos en el siguiente paso)

def registrar_numero(request):
    """
    Vista para registrar un número de lotería.
    Maneja dos situaciones:
    - GET: El usuario llega a la página mostrar el formulario vacío.
    - POST: El usuario envió el formulario validar y guardar los datos.
    """

    if request.method == 'POST':
        # El usuario envió datos creamos el formulario con esos datos
        form = RegistroLoteriaForm(request.POST)

        if form.is_valid():
            # Los datos son válidos guardar en la base de datos
            form.save()
            # Redirigir para evitar doble envío al refrescar la página
            return redirect('loteria:registro_exitoso')

    else:
        # El usuario llegó por primera vez mostrar formulario vacío
        form = RegistroLoteriaForm()

    # Enviamos el formulario al template para renderizarlo
    return render(request, 'loteria/registro.html', {'form': form})


def registro_exitoso(request):
    """
    Vista simple que confirma que el registro fue exitoso.
    """
    return render(request, 'loteria/exito.html')


def home(request):
    """
    Vista de inicio que redirige a la página de registro.
    """
    return redirect('loteria:registrar')
