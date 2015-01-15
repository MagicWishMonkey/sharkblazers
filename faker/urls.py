from django.conf.urls import patterns, url
from faker import views


urlpatterns = patterns(
    '',
    url(r'^$', views.faker, name='faker_home'),
    url(r'^faker/$', views.faker, name='faker_create'),
)
# from accounts import views
#
#
# urlpatterns = patterns('',
#                        url(r'^register/$', views.register, name='register'),
#                        url(r'^profile/$', views.profile, name='profile'),
#                        url(r'^login/$', views.login, name='login'),
#                        url(r'^forgot-password/$', views.forgot_password, name='forgot-password'),
#                        url(r'^activate/(?P<token>[\w\\-]+)/$', views.activate, name='activate'),
#                        url(r'^reset/(?P<token>[\w\\-]+)/$', views.reset_password, name='reset-password'),
#                        url(r'^reset/(?P<token>[\w\\-]+)/forget/$', views.forget_reset_password, name='forget-reset-password'),
#                        )
#
