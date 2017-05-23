from django.conf.urls import url
from views import *          # So we can call functions from our routes!
urlpatterns = [
	url(r'^$', index),
    url(r'^new_product$', new_product)        # 'home' route.
]