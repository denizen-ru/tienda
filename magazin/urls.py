from django.conf.urls import patterns, url
from magazin import views

urlpatterns = patterns('',
    url(r'^$', views.home_page, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^(\d+)/$', views.view_goods, name='view_goods'),
)