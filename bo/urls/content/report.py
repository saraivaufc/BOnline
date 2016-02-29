from django.conf.urls import patterns, include, url

from bo.views.content import Report

report = Report()

urlpatterns = patterns('',
	url(r'^see_all/$', report.see_all, name="content_report_see_all"),
	url(r'^see/(?P<report_id>\d+)/$', report.see, name="content_report_see"),
	url(r'^add/(?P<occurrence_id>\d+)/$', report.add, name="content_report_add"),
	url(r'^edit/(?P<report_id>\d+)/$', report.edit, name="content_report_edit"),
	url(r'^remove/(?P<report_id>\d+)/$', report.remove, name="content_report_remove"),
)