from django.urls import path
from . import views  # Importamos las vistas de esta misma app

# 'app_name' permite usar namespaces para evitar conflictos con otras apps
app_name = 'loteria'

urlpatterns = [
    # Dirección: /loteria/registrar/   llama a la vista registrar_numero
    path('registrar/', views.registrar_numero, name='registrar'),

    # Dirección: /loteria/exito/   llama a la vista registro_exitoso
    path('exito/', views.registro_exitoso, name='registro_exitoso'),
]
