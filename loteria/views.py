from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import RegistroLoteriaForm
from .models import RegistroLoteria

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


def listar_registros(request):
    """
    Vista para listar todos los registros de lotería.
    CU-LT-02: Listar registros de lotería
    Muestra: ID, número, fecha del sorteo, acciones (editar/eliminar)
    """
    # Ordenar por fecha descendente (más recientes primero)
    registros = RegistroLoteria.objects.all().order_by('-fecha')
    
    context = {
        'registros': registros,
        'cantidad': registros.count(),
    }
    
    return render(request, 'loteria/lista_registros.html', context)


def editar_registro(request, id):
    """
    Vista para editar un registro existente.
    CU-LT-03: Actualizar registro de lotería
    - GET: Mostrar formulario precargado con datos actuales
    - POST: Validar y guardar cambios
    """
    # Obtener el registro o mostrar error 404
    registro = get_object_or_404(RegistroLoteria, pk=id)
    
    if request.method == 'POST':
        # El usuario envió cambios
        form = RegistroLoteriaForm(request.POST, instance=registro)
        
        if form.is_valid():
            # Validación exitosa guardar cambios
            form.save()
            return redirect('loteria:listar')
    else:
        # GET: Mostrar formulario con datos del registro
        form = RegistroLoteriaForm(instance=registro)
    
    context = {
        'form': form,
        'registro': registro,
        'es_edicion': True,
    }
    
    return render(request, 'loteria/editar_registro.html', context)


def eliminar_registro(request, id):
    """
    Vista para eliminar un registro existente.
    CU-LT-04: Eliminar registro de lotería
    - GET: Mostrar pantalla de confirmación
    - POST: Eliminar del registro de la base de datos
    """
    # Obtener el registro o mostrar error 404
    registro = get_object_or_404(RegistroLoteria, pk=id)
    
    if request.method == 'POST':
        # Confirmación recibida eliminar el registro
        registro.delete()
        return redirect('loteria:listar')
    
    # GET: Mostrar pantalla de confirmación
    context = {'registro': registro}
    return render(request, 'loteria/confirmar_eliminacion.html', context)


def home(request):
    """
    Vista de inicio que redirige a la página de listado.
    """
    return redirect('loteria:listar')
