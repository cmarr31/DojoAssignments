from django.conf.urls import url # This gives us access to the function url
from . import views # This gives us access to everything (.) in a views.py file that Django automatically created for us when we built our first_app
urlpatterns = [
    url(r'^$', views.index),
	url(r'^projects$', views.projects),
	url(r'^about$', views.about),
	url(r'^testimonials$', views.testimonials)
]