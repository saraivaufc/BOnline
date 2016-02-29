from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required

from bo.utils.decorators import group_required
from bo.models import Occurrence

class Index(object):
	def index(self, request): 
		if request.user.groups.filter(name='organizer').exists():
			return HttpResponseRedirect(reverse('admin'))
		elif request.user.groups.filter(name='general').exists():
			return HttpResponseRedirect(reverse('content'))
		else:
			occurrences = Occurrence.objects.filter(exists=True)
			return render(request, 'bo/index.html', {'is_index':True,'occurrences': occurrences})

	@method_decorator(login_required)
	@method_decorator(group_required('general'))
	def content(self, request):
		occurrences = Occurrence.objects.filter(exists=True)
		return render(request, 'bo/content/content.html', {'is_index':True,'occurrences':occurrences})
	
	@method_decorator(login_required)
	@method_decorator(group_required('organizer'))
	def admin(self, request):
		occurrences = Occurrence.objects.filter(exists=True)
		return render(request, 'bo/admin/admin.html', {'is_index':True,'occurrences':occurrences})

	
	def contact(self, request):
		return HttpResponse("contact")

	def about(self, request):
		return render(request, 'bo/about.html', {})