from django.conf.urls import url
from . import views

def test():
    print """
    
    squeedly woo
    
    """
urlpatterns = [
    url(r'^reset', views.reset),
    url(r'^go_back', views.go_back),
    url(r'^results', views.results),
    url(r'^process', views.process),
    url(r'^', views.main),
]

