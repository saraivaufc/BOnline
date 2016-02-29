from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _

from bo.models import Report, Occurrence
from bo.widgets import AdvancedFileInput

class ReportForm(ModelForm):

	class Meta:
		model= Report
		fields = ("date", "time", "image", "observation")
		widgets = {
			'image': AdvancedFileInput(attrs={}),
		}