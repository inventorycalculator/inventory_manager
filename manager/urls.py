from django.conf.urls import url

from django.contrib.auth.views import login, logout
from manager import views
from manager.forms import LoginForm

urlpatterns = [
    #home
    url(r'^$', views.home, name='home'),

    #signup/signupcomplete
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signup_complete/$', views.signup_complete, name='signup_complete'),

    #login/logout
    url(r'^login/$', login, {
        'authentication_form': LoginForm
        }, name='login'), 
    url(r'^logout/$', logout, {
        'next_page': '/login/', },
    name='logout'),

    #product list/new/edit
    url(r'^product/list/$', views.product_list, name='product_list'),  #Product List
    url(r'^product/(?P<pk>\d+)/$', views.product_detail, name='product_detail'),  #Product Detail
]
