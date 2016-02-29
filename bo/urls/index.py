from django.conf.urls import patterns, include, url

from bo.views.index import Index

index = Index()


urlpatterns = patterns('',
	url(r'^$', index.index, name="index"),
	url(r'^about/$', index.about, name="about"),
)