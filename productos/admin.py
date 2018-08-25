# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Producto, Imagen

# Register your models here.
# admin.site.register(Producto)
admin.site.register(Imagen)

class ImagenInline(admin.TabularInline):
  model = Imagen
  extra = 3

class ProductoAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['nombre', 'descripcion', 'precio']}),
  ]
  inlines = [ImagenInline]
  
admin.site.register(Producto, ProductoAdmin)