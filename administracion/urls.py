"""administracion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
# from django.urls.conf import re_path
from django.views.generic.base import TemplateView
from perfiles.views import SignUpView, BienvenidaView, SignInView, SignOutView
from venta.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', BienvenidaView.as_view(), name='bienvenida'),
    url(r'^registrate/$', SignUpView.as_view(), name='sign_up'),
    url(r'^iniciar-sesion/$', SignInView.as_view(), name='sign_in'),
    url(r'^cerrar-sesion/$', SignOutView.as_view(), name='sign_out'),
    # La ruta 'leer' en donde listamos todos los registros o cliente de la Base de Datos
    path('cliente/', ClienteListado.as_view(template_name = "venta/index_cliente.html"), name='leer_cliente'), 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un cliente o registro 
    #path('cliente/detalle/<int:pk>', ClienteDetalle.as_view(template_name = "venta/detalles_cliente.html"), name='detalles_cliente'), 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo cliente o registro  
    path('cliente/crear', ClienteCrear.as_view(template_name = "venta/crear_cliente.html"), name='crear_cliente'), 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un cliente o registro de la Base de Datos 
    path('cliente/editar/<int:pk>', ClienteActualizar.as_view(template_name = "venta/actualizar_cliente.html"), name='actualizar_cliente'),  
    # La ruta 'eliminar' que usaremos para eliminar un cliente o registro de la Base de Datos 
    path('cliente/eliminar/<int:pk>', ClienteEliminar.as_view(), name='eliminar_cliente'), 
    path('producto/', ProductoListado.as_view(template_name = "venta/index_producto.html"), name='leer_producto'), 
    path('producto/crear', ProductoCrear.as_view(template_name = "venta/crear_producto.html"), name='crear_producto'), 
    path('producto/editar/<int:pk>', ProductoActualizar.as_view(template_name = "venta/actualizar_producto.html"), name='actualizar_producto'), 
    path('producto/eliminar/<int:pk>', ProductoEliminar.as_view(), name='eliminar_producto'), 
    path('ot/', OTListado.as_view(template_name = "venta/index_ot.html"), name='leer_ot'), 
    #path('ot/detalle/<int:pk>', OTDetalle.as_view(template_name = "venta/detalles_ot.html"), name='detalles_ot'),
    path('ot/crear', facturaCrear, name='crear_ot'), 
    path('ot/editar/<int:pk>', OTActualizar.as_view(template_name = "venta/actualizar_ot.html"), name='actualizar_ot'), 
    path('ot/eliminar/<int:pk>', OTEliminar.as_view(), name='eliminar_ot'),
    url(r'^api/$', ventasList.as_view(), name='ventas_list'),
    url(r'^api_detalles/$', detallesList.as_view(), name='detalles_list'),
    url(r'^ventas/$',TemplateView.as_view(template_name="venta/index_venta.html")),
    url(r'^detalles/$',TemplateView.as_view(template_name="venta/detalles_ot.html")),
    #path('ot/detalle/crear/<int:num>', DetalleCrear.as_view(template_name = "venta/crear_detalle.html"), name='crear_detalle'), 
    path('ot/detalle/<int:pk>/', detallesCrearVenta, name="detalles"),
    path('', indexFactura.as_view(template_name = "venta/facturas.html"), name='bienvenida'), 
    # re_path(r'^facturacion/(?P<pk>[0-9])/$', crearFactura, name='crear_factura'),
    url(r'^reporte_facturas_excel/$',ReporteFacturasExcel.as_view(), name="reporte_facturas_excel"),
]
#path('test/<srt:modalidad>', pregunta_views.pregunta, name="test")

# from django.conf.urls import handler404 
handler404 = pag_404_not_found