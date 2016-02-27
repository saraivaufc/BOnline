from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

from bo.forms import OccurrenceForm
from bo.models import Occurrence as OccurrenceModel
from bo.utils.decorators import group_required


class Occurrence():
	
	@method_decorator(login_required)
	@method_decorator(group_required('organizer'))
	def add(self, request):
		if request.method == "POST":
			form = OccurrenceForm(request.POST, request.FILES)
			if form.is_valid():
				occurrence = form.save()
				messages.success(request, _('Occurrence added success.'))
				return HttpResponseRedirect(reverse('admin'))
			else:
				messages.error(request,_('Error adding occurrence.'))
		else:
			form = OccurrenceForm()
		return render(request, 'bo/admin/occurrence/form.html', {'form': form, 'type':'add'})

	@method_decorator(login_required)
	@method_decorator(group_required('organizer'))
	def edit(self, request, occurrence_id):
		try:
			occurrence = OccurrenceModel.objects.get(id=occurrence_id, exists=True)
		except OccurrenceModel.DoesNotExist:
			messages.error(request, 'Occurrence no fount.')
			return HttpResponseRedirect(reverse('admin'))

		if request.method == 'POST':
			form = OccurrenceForm(request.POST, request.FILES, instance=occurrence)
			if form.is_valid():
				occurrence = form.save()
				messages.success(request, _("Successfully edited occurrence"))
				return HttpResponseRedirect(reverse('admin'))
			else:
				messages.error(request, _("Error when editing occurrence"))
		else:
			form = OccurrenceForm(instance=occurrence)
		return render(request, 'bo/admin/occurrence/form.html', 
			{'form': form,
			'occurrence':occurrence, 
			'type':'edit'})

	@method_decorator(login_required)
	@method_decorator(group_required('organizer'))
	def remove(self, request, occurrence_id):
		try:
			occurrence = OccurrenceModel.objects.get(id=occurrence_id, exists=True)
		except OccurrenceModel.DoesNotExist:
			messages.error(request, 'Occurrence no fount.')
			return HttpResponseRedirect(reverse('admin'))
		try:
			occurrence.delete()
			messages.success(request, _('Successfully removed occurrence.'))
		except Exception, e:
			raise(e)
			messages.error(request, _('Error removing occurrence.'))
		return HttpResponseRedirect(reverse('admin'))

	@method_decorator(login_required)
	@method_decorator(group_required('organizer'))
	def restore(self, request, occurrence_id):
		try:
			occurrence = OccurrenceModel.objects.get(id=occurrence_id, exists=False)
		except OccurrenceModel.DoesNotExist:
			messages.error(request, 'Occurrence no fount.')
			return HttpResponseRedirect(reverse('admin'))
		try:
			occurrence.restore()
			messages.success(request, _('Successfully restored occurrence.'))
		except Exception, e:
			raise(e)
			messages.error(request, _('Error restore occurrence.'))
		return HttpResponseRedirect(reverse('admin'))


	@method_decorator(login_required)
	@method_decorator(group_required('organizer'))
	def dump(self, request):
		occurrences = OccurrenceModel.objects.filter(exists=False)
		return render(request, 'bo/admin/occurrence/dump.html', {'occurrences':occurrences})