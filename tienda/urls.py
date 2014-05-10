from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tienda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'magazin.views.home_page', name='home_page'),
    url(r'^magazin/', include('magazin.urls', namespace='magazin')),
    url(r'^admin/', include(admin.site.urls)),
)
