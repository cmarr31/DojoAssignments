from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_page),
    url(r'^register$', views.registration_page),
    url(r'^process_login$', views.authenticate_login),
    url(r'^process_registration$', views.process_registration),
    url(r'^user_page$', views.show_user_home_page),
    url(r'^logout$', views.log_out_user)
]