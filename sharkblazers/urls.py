from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'sharkblazers.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^faker/', include('faker.urls', namespace='faker')),
    url(r'^admin/', include(admin.site.urls)),
)
