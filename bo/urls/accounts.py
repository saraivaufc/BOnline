from django.conf.urls import patterns, include, url

from bo.views.accounts import Accounts

accounts = Accounts()

urlpatterns = patterns('',
	url(r'^$', accounts.login, name='login'),
	url(r'^login/$', accounts.login, name='login'),
	url(r'^logout/$', accounts.logout, name='logout'),
	url(r'^register/$', accounts.register, name='register'),
	url(r'^settings/action=(?P<action>\w+)/$', accounts.settings, name='settings'),
	url(r'^reset/password_reset/$', 'django.contrib.auth.views.password_reset', name='reset_password_reset1'),
	url(r'^reset/password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
	url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
)