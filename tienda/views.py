from django.shortcuts import render
from .models import *
# Create your views here.

def tienda(request):
    productos = Producto.objects.all()
    context ={'productos': productos}
    return render (request, 'tienda/tienda.html', context)

def carrito(request):
    if request.user.is_authenticated :
        cliente = request.user.cliente
        orden, created = Orden.objects.get_or_create(cliente=cliente, complete=False)
        items = orden.orderitem_set.all()
    else:
        items=[]
        orden = {'obtener_carrito_total':0, 'obtener_carrito_items':0}

    context ={'items' :items, 'orden':orden}
    return render (request, 'tienda/carrito.html', context)

def checkout(request):
    if request.user.is_authenticated :
        cliente = request.user.cliente
        orden, created = Orden.objects.get_or_create(cliente=cliente, complete=False)
        items = orden.orderitem_set.all()
    else:
        items=[]
        orden = {'obtener_carrito_total':0, 'obtener_carrito_items':0}

    context ={'items' :items, 'orden':orden}
    return render (request, 'tienda/checkout.html', context)
