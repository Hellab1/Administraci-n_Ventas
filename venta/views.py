from django.shortcuts import render
# Instanciamos las vistas genéricas de Django 
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Instanciamos los modelos para poder usarlo en nuestras Vistas CRUD
from .models import Cliente, Producto, Orden_Compra
# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares 
from django.urls import reverse 
# Habilitamos el uso de mensajes en Django
from django.contrib import messages  
# Habilitamos los mensajes para class-based views 
from django.contrib.messages.views import SuccessMessageMixin  
# Habilitamos los formularios en Django
from django import forms

# Create your views here.
class ClienteListado(ListView): 
    model = Cliente # Llamamos a la clase 'Cliente' que se encuentra en nuestro archivo 'models.py'

class ClienteCrear(SuccessMessageMixin, CreateView): 
    model = Cliente # Llamamos a la clase 'Cliente' que se encuentra en nuestro archivo 'models.py'
    form = Cliente # Definimos nuestro formulario con el nombre de la clase o modelo 'Cliente'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Cliente' de nuestra Base de Datos 
    success_message = 'Cliente Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Cliente
 
    # Redireccionamos a la página principal luego de crear un registro o Cliente
    def get_success_url(self):        
        return reverse('leer_cliente') # Redireccionamos a la vista principal 'leer'

class ClienteDetalle(DetailView): 
    model = Cliente # Llamamos a la clase 'Cliente' que se encuentra en nuestro archivo 'models.py'

class ClienteActualizar(SuccessMessageMixin, UpdateView): 
    model = Cliente # Llamamos a la clase 'Cliente' que se encuentra en nuestro archivo 'models.py' 
    form = Cliente # Definimos nuestro formulario con el nombre de la clase o modelo 'Cliente' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Cliente' de nuestra Base de Datos 
    success_message = 'Cliente Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Cliente 
 
    # Redireccionamos a la página principal luego de actualizar un registro o Cliente
    def get_success_url(self):               
        return reverse('leer_cliente') # Redireccionamos a la vista principal 'leer'

class ClienteEliminar(SuccessMessageMixin, DeleteView): 
    model = Cliente 
    form = Cliente
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o Cliente
    def get_success_url(self): 
        success_message = 'Cliente Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Cliente 
        messages.success (self.request, (success_message))       
        return reverse('leer_cliente') # Redireccionamos a la vista principal 'leer'

class ProductoListado(ListView): 
    model = Producto

class ProductoCrear(SuccessMessageMixin, CreateView): 
    model = Producto
    form = Producto
    fields = "__all__" 
    success_message = 'Producto Creado Correctamente !' 

    def get_success_url(self):        
        return reverse('leer_producto') 

class ProductoDetalle(DetailView): 
    model = Producto 

class ProductoActualizar(SuccessMessageMixin, UpdateView): 
    model = Producto 
    form = Producto
    fields = "__all__"
    success_message = 'Producto Actualizado Correctamente !' 

    def get_success_url(self):               
        return reverse('leer_producto') 

class ProductoEliminar(SuccessMessageMixin, DeleteView): 
    model = Producto 
    form = Producto
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Producto Eliminado Correctamente !'
        messages.success (self.request, (success_message))       
        return reverse('leer_producto') 

class OTListado(ListView): 
    model = Orden_Compra

class OTCrear(SuccessMessageMixin, CreateView): 
    model = Orden_Compra
    form = Orden_Compra
    fields = "__all__" 
    success_message = 'Orden de Compra Creada Correctamente !' 

    def get_success_url(self):        
        return reverse('leer_ot') 

class OTDetalle(DetailView): 
    model = Orden_Compra 

class OTActualizar(SuccessMessageMixin, UpdateView): 
    model = Orden_Compra 
    form = Orden_Compra
    fields = "__all__"
    success_message = 'Orden de Compra Actualizada Correctamente !' 

    def get_success_url(self):               
        return reverse('leer_ot') 

class OTEliminar(SuccessMessageMixin, DeleteView): 
    model = Orden_Compra 
    form = Orden_Compra
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Orden de Compra Eliminada Correctamente !'
        messages.success (self.request, (success_message))       
        return reverse('leer_ot') 