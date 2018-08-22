# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return render(request, 'productos/index.html')

def empresa(request):
  return HttpResponse("empresa")

def productos(request):
  return HttpResponse("productos")

def contacto(request):
  return HttpResponse("contacto")
