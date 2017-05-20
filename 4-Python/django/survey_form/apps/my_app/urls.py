from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit_survey$', views.submit_survey),
    url(r'^result$', views.result)
]