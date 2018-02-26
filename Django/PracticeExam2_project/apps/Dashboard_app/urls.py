from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'^user/(?P<getUserID>\d+)$', views.user),
]
