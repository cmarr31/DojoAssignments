from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new_course$', views.create_new_course),
    url(r'^delete_course/(?P<course_id>\d+)', views.show_delete_confirmation),
    url(r'^confirm_delete/(?P<course_id>\d+)', views.delete_course)
]
