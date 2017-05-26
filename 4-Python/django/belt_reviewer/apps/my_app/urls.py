from django.conf.urls import url
from . import views
# from views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register', views.register, name='register'),
    url(r'^landing_page$', views.landing_page, name='landing_page'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^new_book$', views.show_add_book_page, name='new_book'),
    url(r'^process_add_book$', views.process_add_book, name='process_add_book'),
    url(r'^book/(?P<book_id>\d+)$', views.show_book_page, name='book_page'),
    url(r'^user/(?P<user_id>\d+)$', views.show_user_profile, name='user_page'),
    url(r'^add_review/(?P<book_id>\d+)$', views.add_review, name='add_review'),
    url(r'^delete_review/(?P<review_id>\d+)$', views.delete_review, name='delete_review'),
    url(r'^add_to_my_favorites/(?P<book_id>\d+)$', views.add_to_my_favorites, name='add_to_my_favorites')    
]