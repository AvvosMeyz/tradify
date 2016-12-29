from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nice/(?P<user_id>\d+)$', views.nice, name='nice'),
    url(r'^nope/(?P<user_id>\d+)$', views.nope, name='nope'),
]
