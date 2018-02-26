from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^test$', views.test),
    url(r'courses/create$', views.create),
    url(r'^courses/(?P<courseID>\d+)/confirm$', views.confirm),
    url(r'^courses/(?P<courseID>\d+)/delete$', views.delete),
]