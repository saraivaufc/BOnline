from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone

class Occurrence(models.Model):
	name = models.CharField(max_length=255, verbose_name=_("Name"), help_text=_("enter the name of the event. Example: theft, damage, etc."))
	description = models.TextField(verbose_name=_("Description"), help_text=_("enter a description for the event. Example to be given: to destroy, render useless or deteriorate alien thing."))
	