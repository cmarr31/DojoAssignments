from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.validation_check),
    url(r'^emails$', views.display_email_list),
    url(r'^emails/(?P<email_id>\d+)/delete$', views.delete_email)
]
