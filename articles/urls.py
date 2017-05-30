from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^add$', views.add, name='add'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit, name='edit'),
    url(r'^detail/(?P<article_id>[0-9]+)$', views.detail, name='detail'),
]
