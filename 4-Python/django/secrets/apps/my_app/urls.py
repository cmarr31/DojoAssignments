from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_page, name="login_page"),
    url(r'^register$', views.registration_page, name="registration_page"),
    url(r'^process_login$', views.authenticate_login, name="process_login"),
    url(r'^process_registration$', views.process_registration, name="process_registration"),
    url(r'^logout$', views.log_out_user, name="logout"),
    url(r'^secrets$', views.show_secret_page, name="secrets"),
    url(r'^new_secret/(?P<user_id>\d+)$', views.create_new_secret, name="new_secret"),
    url(r'^delete_secret/(?P<secret_id>\d+)/(?P<return_loc>\w+)$', views.delete_secret, name="delete_secret"),
    url(r'^like_secret/(?P<secret_id>\d+)/(?P<user_id>\d+)/(?P<return_loc>\w+)$', views.like_secret, name="like_secret"),
    url(r'^unlike_secret/(?P<secret_id>\d+)/(?P<user_id>\d+)/(?P<return_loc>\w+)$', views.unlike_secret, name="unlike_secret"),
    url(r'^most_popular', views.show_most_popular, name="most_popular")
]