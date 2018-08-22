# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Producto, ImagenProducto

# Register your models here.
# admin.site.register(Producto)
admin.site.register(ImagenProducto)

class ImagenInline(admin.TabularInline):
  model = ImagenProducto
  extra = 3

class ProductoAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['nombre', 'descripcion', 'precio']}),
  ]
  inlines = [ImagenInline]
  
admin.site.register(Producto, ProductoAdmin)