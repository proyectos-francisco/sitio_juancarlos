from django.conf.urls import url

from . import views

app_name = 'productos'
urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^productos/', views.productos, name='productos'),
  url(r'^empresa/', views.empresa, name='empresa'),
  url(r'^contacto/', views.contacto, name='contacto'),
]
