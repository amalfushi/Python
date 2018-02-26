from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test$', views.test),
    url(r'^$', views.main),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
]