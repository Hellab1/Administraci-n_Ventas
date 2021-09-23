from django.http.response import Http404
from django.shortcuts import render
# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Instanciamos los modelos para poder usarlo en nuestras Vistas CRUD
from .models import Cliente, Detalle_Venta, Producto, Orden_Compra
# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages  
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin  
# Habilitamos los formularios en Django
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import generics
from .serializers import detallesSerializer, ventaSerializer

# Create your views here.
class ClienteListado(LoginRequiredMixin, ListView): 
    model = Cliente # Llamamos a la clase 'Cliente' que se encuentra en nuestro archivo 'models.py'
    login_url = '/iniciar-sesion/'
class ClienteCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    model = Cliente # Llamamos a la clase 'Cliente' que se encuentra en nuestro archivo 'models.py'
    form = Cliente # Definimos nuestro formulario con el nombre de la clase o modelo 'Cliente'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Cliente' de nuestra Base de Datos 
    success_message = 'Cliente Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Cliente
    login_url = '/iniciar-sesion/'
    # Redireccionamos a la página principal luego de crear un registro o Cliente
    def get_success_url(self):        
        return reverse('leer_cliente') # Redireccionamos a la vista principal 'leer'

"""class ClienteDetalle(LoginRequiredMixin, DetailView): 
    model = Cliente # Llamamos a la clase 'Cliente' que se encuentra en nuestro archivo 'models.py'
    login_url = '/iniciar-sesion/' """

class ClienteActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = Cliente # Llamamos a la clase 'Cliente' que se encuentra en nuestro archivo 'models.py' 
    form = Cliente # Definimos nuestro formulario con el nombre de la clase o modelo 'Cliente' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Cliente' de nuestra Base de Datos 
    success_message = 'Cliente Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Cliente 
    login_url = '/iniciar-sesion/' 
    # Redireccionamos a la página principal luego de actualizar un registro o Cliente
    def get_success_url(self):               
        return reverse('leer_cliente') # Redireccionamos a la vista principal 'leer'

class ClienteEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = Cliente 
    form = Cliente
    fields = "__all__"     
    login_url = '/iniciar-sesion/' 
    # Redireccionamos a la página principal luego de eliminar un registro o Cliente
    def get_success_url(self): 
        success_message = 'Cliente Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Cliente 
        messages.success (self.request, (success_message))       
        return reverse('leer_cliente') # Redireccionamos a la vista principal 'leer'

class ProductoListado(LoginRequiredMixin, ListView): 
    model = Producto
    login_url = '/iniciar-sesion/'

class ProductoCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    model = Producto
    form = Producto
    fields = "__all__" 
    success_message = 'Producto Creado Correctamente !' 
    login_url = '/iniciar-sesion/'
    def get_success_url(self):        
        return reverse('leer_producto') 

class ProductoActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = Producto 
    form = Producto
    fields = "__all__"
    success_message = 'Producto Actualizado Correctamente !' 
    login_url = '/iniciar-sesion/'
    def get_success_url(self):               
        return reverse('leer_producto') 

class ProductoEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = Producto 
    form = Producto
    fields = "__all__"     
    login_url = '/iniciar-sesion/'
    def get_success_url(self): 
        success_message = 'Producto Eliminado Correctamente !'
        messages.success (self.request, (success_message))       
        return reverse('leer_producto') 

class OTListado(LoginRequiredMixin, ListView): 
    model = Orden_Compra
    login_url = '/iniciar-sesion/'

class OTCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    model = Orden_Compra
    form = Orden_Compra
    fields = "__all__" 
    success_message = 'Orden de Compra Creada Correctamente!' 
    login_url = '/iniciar-sesion/'
    def get_success_url(self):        
        return reverse('leer_ot') 
"""
class OTDetalle(LoginRequiredMixin, DetailView): 
    model = Orden_Compra
    login_url = '/iniciar-sesion/'
"""
class OTActualizar(LoginRequiredMixin, SuccessMessageMixin, UpdateView): 
    model = Orden_Compra 
    form = Orden_Compra
    fields = "__all__"
    success_message = 'Orden de Compra Actualizada Correctamente !' 
    login_url = '/iniciar-sesion/'
    def get_success_url(self):               
        return reverse('leer_ot') 

class OTEliminar(LoginRequiredMixin, SuccessMessageMixin, DeleteView): 
    model = Orden_Compra 
    form = Orden_Compra
    fields = "__all__"   
    login_url = '/iniciar-sesion/' 
    def get_success_url(self): 
        success_message = 'Orden de Compra Eliminada Correctamente !'
        messages.success (self.request, (success_message))       
        return reverse('leer_ot') 

class DetalleCrear(LoginRequiredMixin, SuccessMessageMixin, CreateView): 
    model = Detalle_Venta
    form = Detalle_Venta
    fields = "__all__" 
    success_message = 'Detalle Creado Correctamente !' 
    login_url = '/iniciar-sesion/'
    def get_success_url(self):        
        return reverse('leer_ot') 

class ventasList(generics.ListAPIView):
    queryset = Orden_Compra.objects.all()
    serializer_class = ventaSerializer

class detallesList(generics.ListAPIView):
    queryset = Orden_Compra.objects.all()
    serializer_class = detallesSerializer


def pregunta(request, pk):
    productos = Producto.objects.all()
    details = Detalle_Venta.objects.filter(orden_venta=pk)
    return render(request, "venta/detalles_venta.html", {'details':details, 'productos':productos})

    

