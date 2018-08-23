# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Producto

#TODO: traer html a los templates
#TODO: agregar scss
#TODO: remodelar admin
#TODO: deploy

def index(request):
  return render(request, 'productos/index.html', {
    'current': 'index',
  })

def empresa(request):
  return render(request, 'productos/empresa.html', {
    'current': 'empresa',
  })

def productos(request):
  productos_list = Producto.objects.all()
  return render(request, 'productos/productos.html', {
    'current': 'productos',
    'productos': productos_list,
  })
def contacto(request):
  return render(request, 'productos/contacto.html', {
    'current': 'contacto',
  })
