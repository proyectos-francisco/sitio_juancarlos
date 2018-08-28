# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Producto, Imagen
from django.utils.safestring import mark_safe
from imagekit.admin import AdminThumbnail

# Register your models here.
# admin.site.register(Producto)

class ImagenInline(admin.TabularInline):
  model = Imagen
  extra = 3

  admin_thumbnail = AdminThumbnail(image_field='imagen')
  admin_thumbnail.short_description = 'Imagen previa'
  fields = ['descripcion','imagen','admin_thumbnail']
  readonly_fields = ['admin_thumbnail']


class ProductoAdmin(admin.ModelAdmin):
  list_display = ('nombre', 'fecha_publicacion')
  fieldsets = [
    (None, {'fields': ['nombre', 'descripcion', 'precio']}),
  ]
  inlines = [ImagenInline]
  
admin.site.register(Producto, ProductoAdmin)