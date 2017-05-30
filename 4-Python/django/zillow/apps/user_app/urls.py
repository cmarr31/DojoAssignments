from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  
    url(r'^join$', views.join, name='join'),
    url(r'^sign_in$', views.sign_in, name='sign_in'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^register', views.register, name='register'),
    url(r'^user/(?P<user_id>\d+)$', views.show_user_profile, name='user_page'),
]