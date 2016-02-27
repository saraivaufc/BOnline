from django.conf.urls import patterns, include, url

from bo.views.index import Index

index = Index()

urlpatterns = patterns('',
	url(r'^$', index.admin, name="admin"),
    url(r'^occurrence/', include('bo.urls.admin.occurrence')),
)