from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),  
    url(r'^new_listing$', views.new_listing, name='new_listing'),
    url(r'^create_listing$', views.create_listing, name='create_listing'),
    # url(r'^listing$', views.index, name='index'),  
    # url(r'^landing_page$', views.landing_page, name='landing_page'),
    # url(r'^user/(?P<user_id>\d+)$', views.show_user_profile, name='user_page'),
    # url(r'^add_to_my_favorites/(?P<quote_id>\d+)$', views.add_to_my_favorites, name='add_to_my_favorites'),
    # url(r'^remove_from_my_favorites/(?P<quote_id>\d+)$', views.remove_from_my_favorites, name='remove_from_my_favorites')
]