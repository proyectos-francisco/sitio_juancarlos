from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'productos'
urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^productos/', views.productos, name='productos'),
  url(r'^empresa/', views.empresa, name='empresa'),
  url(r'^contacto/', views.contacto, name='contacto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
