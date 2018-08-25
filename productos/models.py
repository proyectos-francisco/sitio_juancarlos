# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Producto(models.Model):
  nombre = models.CharField("Nombre", max_length=50)
  descripcion = models.CharField("Descripcion", max_length=250)
  precio = models.IntegerField("Precio")

  def __str__(self):
      return self.nombre
  

class Imagen(models.Model):
  producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='lista_imagenes')
  descripcion = models.CharField("Descripcion de la imagen", max_length=150)
  imagen = models.ImageField("Imagen", upload_to='fotos_productos', height_field=None, width_field=None, max_length=None)
  
  def __str__(self):
      return self.descripcion