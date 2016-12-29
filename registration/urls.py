from django.conf.urls import url
from registration import views

# /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/', views.register, name='register'),
]
