from django.conf.urls import patterns, include, url

from bo.views.index import Index

index = Index()

urlpatterns = patterns('',
	url(r'^$', index.content, name="content"),
    url(r'^report/', include('bo.urls.content.report')),
)