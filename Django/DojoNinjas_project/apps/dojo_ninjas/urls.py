from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^', views.main),
    # url(r'^admin/', admin.site.urls),
]