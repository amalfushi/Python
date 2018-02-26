from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reset', views.reset),
    url(r'^checkout$', views.checkout),
    url(r'^buy$', views.buy),
    url(r'^$', views.main),
]
