from ast import Delete
import email
from pyexpat import model
from re import I, template
from django.forms import model_to_dict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from django.urls import reverse_lazy
from AppTP.models import Producto, Proveedor, Cliente
from AppTP.forms import ProductosForm, ClientesForm, CargaproductosForm
from AppTP.forms import ProductosForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

def inicio(request):
    
      return render(request, "AppTP/inicio.html")
  
def clientes(request):
    
      return render(request, "AppTP/clientes.html", {"Cliente": Cliente.objects.all()})
  
def productos(request):
    
      return render(request, "AppTP/productos.html", {"producto": Producto.objects.all()})
  
def proveedores(request):
    
      return render(request, "AppTP/proveedores.html", {"proveedor": Proveedor.objects.all()})

def formulariocliente(request):
    
      if request.method == "POST":
      
            formulario_cliente = ClientesForm(request.POST) 
            
            if formulario_cliente.is_valid():
                  data= formulario_cliente.cleaned_data
                  Cliente.objects.create(nombre=data["nombre"], apellido=data["apellido"], email=data["email"],dni=data["dni"])
                  return redirect("Clientes")
      else:
            formulario_cliente = ClientesForm()

      return render(request, "AppTP/formulario_clientes.html", {"formulario_cliente":formulario_cliente})


def formulariocargaproducto(request):
    
      if request.method == "POST":
      
            formulario_carga_producto = CargaproductosForm(request.POST) 
            
            if formulario_carga_producto.is_valid():
                  data= formulario_carga_producto.cleaned_data
                  Producto.objects.create(nombre=data["nombre"], marca=data["marca"], codigo=data["codigo"],precio=data["precio"], cantidad=data["cantidad"])
                  return redirect("Productos")
      else:
            formulario_carga_producto = CargaproductosForm()

      return render(request, "AppTP/formulario_carga_producto.html", {"formulario_carga_producto":formulario_carga_producto})
# 
  
def busquedaproducto(request):
      return render(request, "AppTP/busquedaproducto.HTML")
  
def buscar(request):
    
    if request.GET["codigo"]:
        codigo = request.GET["codigo"]
        producto = Producto.objects.filter(codigo=codigo)
        # nombre = Producto.objects.filter(codigo=codigo)
        # marca = Producto.objects.filter(codigo=codigo)
        # precio = Producto.objects.filter(codigo=codigo)
        # cantidad = Producto.objects.filter(codigo=codigo)
        
        return render(request, "AppTP/buscar.html", {"codigo":codigo, "producto":producto})
    
    else:
        
        respuesta = "No ingresaste Datos"
    
    return HttpResponse(respuesta)

# def eliminarproducto (request, codigo):
#       producto = Producto.objects.get(codigo=codigo)
#       producto.delete()
      
#       productos = Producto.objects.all()
      
#       contexto = {"productos":productos}
      
#       return render (request, "AppTP/productos.html", contexto)

def producto_delete (request, id_producto):
      producto = Producto.objects.get(id = id_producto)
      producto.delete()
      return redirect("Productos")

def producto_update (request, id_producto):
      producto = Producto.objects.get(id = id_producto)
      
      if request.method == "POST":
          
            formulario_carga_producto = CargaproductosForm(request.POST) 
            
            if formulario_carga_producto.is_valid():
                  data= formulario_carga_producto.cleaned_data
                  
                  producto.nombre=data["nombre"]
                  producto.marca=data["marca"]
                  producto.codigo=data["codigo"]
                  producto.precio=data["precio"] 
                  producto.cantidad=data["cantidad"]
                  producto.save()
                  
                  return redirect("Productos")
      else:
            formulario_carga_producto = CargaproductosForm(model_to_dict(producto))

      return render(request, "AppTP/formulario_carga_producto.html", {"formulario_carga_producto":formulario_carga_producto})



class ProveedoresListView(ListView):
      model = Proveedor
      template_name = "AppTP/proveedores.html"
      context_object_name = "proveedor"
      
class ProveedoresDetailView(DetailView):
      model = Proveedor
      template_name = "AppTP/ver_proveedor.html"
      
      
class ProveedoresCreateView(CreateView):
      model = Proveedor 
      success_url = reverse_lazy("Proveedores")
      fields = ["cuil", "nombre", "provincia"]
      template_name = "AppTP/proveedores_form.html"


class ProveedoresUpdateView(UpdateView):
      model = Proveedor 
      success_url = reverse_lazy("Proveedores")
      fields = ["cuil", "nombre", "provincia"]
      template_name = "AppTP/proveedores_form.html"

class ProveedoresDeleteView(DeleteView):
      model = Proveedor
      success_url = reverse_lazy("Proveedores")
      template_name = "AppTP/proveedor_delete.html"