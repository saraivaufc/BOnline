from django.conf.urls import patterns, include, url

from bo.views.admin import Occurrence

occurrence = Occurrence()

urlpatterns = patterns('',
	url(r'^add/$', occurrence.add, name="admin_occurrence_add"),
	url(r'^edit/(?P<occurrence_id>\d+)/$', occurrence.edit, name="admin_occurrence_edit"),
	url(r'^remove/(?P<occurrence_id>\d+)/$', occurrence.remove, name="admin_occurrence_remove"),
	url(r'^restore/(?P<occurrence_id>\d+)/$', occurrence.restore, name="admin_occurrence_restore"),
	url(r'^dump/$', occurrence.dump, name="admin_occurrence_dump"),
	
)