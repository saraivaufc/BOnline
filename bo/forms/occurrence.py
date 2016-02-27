from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _

from bo.models import Occurrence
from bo.widgets import AdvancedFileInput
class OccurrenceForm(ModelForm):
	class Meta:
		model= Occurrence
		fields = ("name","description", "image")
		widgets = {
            'image': AdvancedFileInput(attrs={}),
        }