from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reset', views.reset),
    url(r'^process', views.process),
    url(r'^', views.main),
]
