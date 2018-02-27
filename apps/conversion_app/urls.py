from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),
    url(r'^multiply$', views.multiply),
    url(r'^divide$', views.divide)
  ]