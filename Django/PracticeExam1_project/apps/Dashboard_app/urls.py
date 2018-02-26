from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'^(?P<getUserID>\d+)$', views.user),
    url(r'^add$', views.add)
]
