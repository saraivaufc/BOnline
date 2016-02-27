from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone

class Occurrence(models.Model):
	name = models.CharField(max_length=255, 
							verbose_name=_("Name"), 
							help_text=_("enter the name of the event. Example: theft, damage, etc."), 
							unique=True)
	description = models.TextField(verbose_name=_("Description"), 
									help_text=_("enter a description for the event. Example to be given: to destroy, render useless or deteriorate alien thing."))
	image = models.ImageField(verbose_name=_(u"Image"),
							help_text=_(u"Please enter image to occurrence."),
							upload_to = 'documents/image/occurrence/%Y/%m/%d')
	
	
	creation = models.DateTimeField(verbose_name=_(u'Creation'), default=timezone.now)
	exists = models.BooleanField(verbose_name=_(u"Exists"), default=True)


	def get_name(self):
		return self.name

	def get_description(self):
		return self.description

	def get_image(self):
		return self.image

	def __unicode__(self):
		return self.name

	def delete(self):
		self.exists = False
		self.save()
		
	def restore(self):
		self.exists = True
		self.save()
	
	class Meta:
		ordering = ['name']
		verbose_name = _(u"Occurrence")
		verbose_name_plural = _(u"Occurrences")

