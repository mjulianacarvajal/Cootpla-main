
from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"), name="redirect-admin"),
    path('login', auth_views.LoginView.as_view(template_name="login.html", redirect_authenticated_user=True),name='login'),
    path('login_user', views.login_user, name="login-user"),
    path('registrarUsuario', views.registrarUsuario, name="registrar-usuario"),
    path('logout', views.logoutuser, name='logout'),

    path('perfil', views.perfil, name='perfil'),
    path('actualizarPerfil', views.actualizarPerfil, name='actualizar_perfil'),
    path('actualizarContrasena', views.actualizarContrasena, name='actualizar_contrasena'),


    path('', views.inicio, name='inicio'),

    path('sede', views.sede, name='sede-pagina'),
    path('adm_sede', views.adm_sede, name='adm-sede'),
    path('guardar_sede', views.guardar_sede, name='guardar-sede'),
    path('adm_sede/<int:pk>', views.adm_sede, name='adm-sede-pk'),
    path('eliminar_sede', views.eliminar_sede, name='eliminar-sede'),


   #
    path('vehiculo', views.vehiculo, name='vehiculo-pagina'),
    path('adm_vehiculo', views.adm_vehiculo, name='adm-vehiculo'),
    path('guardar_vehiculo', views.guardar_vehiculo, name='guardar-vehiculo'),
    path('adm_vehiculo/<int:pk>', views.adm_vehiculo, name='adm-vehiculo-pk'),
    path('eliminar_vehiculo', views.eliminar_vehiculo, name='eliminar-vehiculo'),

   #
    path('programacion', views.programacion, name='programacion-pagina'),
    path('adm_programacion', views.adm_programacion, name='adm-programacion'),
    path('guardar_programacion',views.guardar_programacion,name='guardar-programacion'),
    path('adm_programacion/<int:pk>',views.adm_programacion,name='adm-programacion-pk'),
    path('eliminar_programacion', views.eliminar_programacion, name='eliminar-programacion'),

    #
    path('encomienda', views.encomienda, name='encomienda-pagina'),
    path('adm_encomienda', views.adm_encomienda, name='adm-encomienda'),
    path('guardar_encomienda',views.guardar_encomienda,name='guardar-encomienda'),
    path('adm_encomienda/<int:pk>',views.adm_encomienda,name='adm-encomienda-pk'),
    path('eliminar_encomienda', views.eliminar_encomienda, name='eliminar-encomienda'),

    #
    path('viajes_programados',views.viajes_programados,name='viajes-programados-pagina'),
    path('buscar_programado', views.buscar_programado, name='buscar-viaje-programado'),

    path('', views.base),

    path('contacto', views.contacto, name="contacto"),
]

