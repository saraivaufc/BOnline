from django.conf.urls import patterns, include, url

from bo.views.index import Index

index = Index()

urlpatterns = patterns('',
	url(r'^', include('bo.urls.index')),
	url(r'^index/', include('bo.urls.index')),
	url(r'^content/', include('bo.urls.content')),
	url(r'^admin/', include('bo.urls.admin')),
    url(r'^accounts/', include('bo.urls.accounts')),
)