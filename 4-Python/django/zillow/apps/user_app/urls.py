from django.conf.urls import url
from . import views
# from views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),  
    # url(r'^login$', views.login, name='login'),
    # url(r'^logout$', views.logout, name='logout'),
    # url(r'^register', views.register, name='register'),
]