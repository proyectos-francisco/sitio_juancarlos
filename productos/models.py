# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from os.path import splitext, join
import uuid

class Producto(models.Model):
  nombre = models.CharField("Nombre", max_length=50)
  descripcion = models.CharField("Descripcion", max_length=250)
  precio = models.IntegerField("Precio")
  
  fecha_publicacion = models.DateTimeField('Fecha de publicacion', default=timezone.now)
  
  def __str__(self):
      return self.nombre
  

def unique_file_path(instance, filename):
  # save original file name in model
  instance.original_file_name = filename

  # save new name
  base, ext = splitext(filename)
  new_name = "%s%s" % (uuid.uuid4(), ext)
  return join('fotos_productos', new_name)

class Imagen(models.Model):
  producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='lista_imagenes')
  descripcion = models.CharField("Descripcion de la imagen", max_length=150)
  imagen = models.ImageField("Imagen", upload_to=unique_file_path)
  original_file_name = models.CharField("Nombre original", max_length=250, editable=False)
  thumbnail = ImageSpecField(source='imagen',
                            processors=[ResizeToFill(300, 300)],
                            format='JPEG',
                            options={'quality': 90})

  def __str__(self):
      return self.descripcion

  