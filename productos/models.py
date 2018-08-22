# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Producto(models.Model):
  nombre = models.CharField("Nombre", max_length=50)
  descripcion = models.CharField("Descripcion", max_length=250)
  precio = models.IntegerField("Precio")

class ImagenProducto(models.Model):
  producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes')
  imagen = models.ImageField("Imagen", upload_to=None, height_field=None, width_field=None, max_length=None)
