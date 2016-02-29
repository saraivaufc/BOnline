from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

from bo.forms import ReportForm, AddressForm
from bo.models import Report as ReportModel
from bo.models import Occurrence as OccurrenceModel
from bo.utils.decorators import group_required


class Report():
	@method_decorator(login_required)
	@method_decorator(group_required('general'))
	def see_all(self, request):
		reports = ReportModel.objects.filter(exists=True, person = request.user)
		return render(request, 'bo/content/report/see_all.html', {'is_my_reports': True, 'reports':reports})


	@method_decorator(login_required)
	@method_decorator(group_required('general'))
	def see(self, request, report_id):
		if request.method == "POST":
			form = ReportForm(request.POST, request.FILES)
			if form.is_valid():
				report = form.save()
				messages.success(request, _('Report added success.'))
				return HttpResponseRedirect(reverse('content'))
			else:
				messages.error(request,_('Error adding report.'))
		else:
			form = ReportForm()
		return render(request, 'bo/content/report/form.html', {'form': form, 'type':'add'})



	@method_decorator(login_required)
	@method_decorator(group_required('general'))
	def add(self, request,  occurrence_id):
		try:
			occurrence = OccurrenceModel.objects.get(id=occurrence_id, exists=True)
		except OccurrenceModel.DoesNotExist:
			messages.error(request, 'Occurrence no fount.')
			return HttpResponseRedirect(reverse('content'))

		if request.method == "POST":
			form_address = AddressForm(request.POST, prefix='address')
			form_report = ReportForm(request.POST, request.FILES, prefix='report')
			if form_address.is_valid() and form_report.is_valid():
				address = form_address.save()
				report = form_report.save(commit=False)
				
				report.set_address(address)
				report.set_person(request.user)
				report.set_occurrence(occurrence)

				report.save()
				messages.success(request, _('Report added success.'))
				return HttpResponseRedirect(reverse('content_report_see_all'))
			else:
				messages.error(request,_('Error adding report.'))
		else:
			form_address = AddressForm(prefix='address')
			form_report = ReportForm(prefix='report')
		return render(request, 'bo/content/report/form.html', {
			'form_report': form_report,
			'form_address': form_address, 
			'type':'add', 
			'occurrence': occurrence
			})

	@method_decorator(login_required)
	@method_decorator(group_required('general'))
	def edit(self, request, report_id):
		print request
		try:
			report = ReportModel.objects.get(id=report_id, exists=True)
		except ReportModel.DoesNotExist:
			messages.error(request, 'Report no fount.')
			return HttpResponseRedirect(reverse('content'))

		if request.method == "POST":
			form_address = AddressForm(request.POST, prefix='address', instance=report.get_address())
			form_report = ReportForm(request.POST, request.FILES, prefix='report', instance=report)
			if form_address.is_valid() and form_report.is_valid():
				address = form_address.save()
				
				report = form_report.save(commit=False)
				report.set_person(report.get_person())
				report.set_occurrence(report.get_occurrence())

				report.save()
				messages.success(request, _('Successfully edited report'))
				return HttpResponseRedirect(reverse('content_report_see_all'))
			else:
				messages.error(request,_('Error when editing report.'))
		else:
			form_address = AddressForm(prefix='address', instance=report.get_address())
			form_report = ReportForm(prefix='report', instance=report)

		return render(request, 'bo/content/report/form.html', 
			{'form_report': form_report,
			'form_address': form_address,
			'report':report,
			'occurrence': report.get_occurrence(), 
			'type':'edit',
			'is_my_reports':True})

	@method_decorator(login_required)
	@method_decorator(group_required('general'))
	def remove(self, request, report_id):
		try:
			report = ReportModel.objects.get(id=report_id, exists=True)
		except ReportModel.DoesNotExist:
			messages.error(request, 'Report no fount.')
			return HttpResponseRedirect(reverse('content'))
		try:
			report.delete()
			messages.success(request, _('Successfully removed report.'))
			return HttpResponseRedirect(reverse('content_report_see_all'))
		except Exception, e:
			raise(e)
			messages.error(request, _('Error removing report.'))
		return HttpResponseRedirect(reverse('content'))