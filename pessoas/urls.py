from django.conf.urls import url
from pessoas import views

urlpatterns = [
    url(r'^api/pessoas$', views.pessoa_list),
    url(r'^api/pessoas/(?P<pk>[0-9]+)$', views.pessoa_detail)
]