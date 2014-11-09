from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from wish.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wish.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^add/', add),
    url(r'^auto/$', auto),
    url(r'^bank/$', bank),
    url(r'^delete/$', delete),
    url(r'^read/$', read),

)
