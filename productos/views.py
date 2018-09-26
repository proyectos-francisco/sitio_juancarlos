# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Producto

#TODO: remodelar admin
#TODO: deploy

def index(request):
  productos_list = Producto.objects.order_by('-fecha_publicacion')[:4]
  return render(request, 'productos/index.html', {
    'current': 'index',
    'productos': productos_list,
  })

def empresa(request):
  return render(request, 'productos/empresa.html', {
    'current': 'empresa',
  })

def productos(request):
  productos_list = Producto.objects.order_by('-fecha_publicacion')
  return render(request, 'productos/productos.html', {
    'current': 'productos',
    'productos': productos_list,
  })

def contacto(request):
  return render(request, 'productos/contacto.html', {
    'current': 'contacto',
  })

def handler404(request):
  return render(request, 'productos/404.html')