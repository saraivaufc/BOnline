from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required

from bo.utils.decorators import group_required

class Index(object):
	
	def index(self, request): 
		if request.user.groups.filter(name='organizer').exists():
			return HttpResponseRedirect(reverse('admin'))
		elif request.user.groups.filter(name='generalUser').exists():
			return HttpResponseRedirect(reverse('content'))
		else:
			return render(request, 'bo/index.html', {})

	@method_decorator(login_required)
	@method_decorator(group_required('generalUser'))
	def content(self, request):
		return render(request, 'bo/content/content.html', {})
	
	@method_decorator(login_required)
	@method_decorator(group_required('organizer'))
	def admin(self, request):
		return render(request, 'bo/admin/admin.html', {})

	
	def contact(self, request):
		return HttpResponse("contact")

	def about(self, request):
		return HttpResponse("about")