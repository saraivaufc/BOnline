from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone

class Report(models.Model):
	person = models.ForeignKey('Person', verbose_name=_(u"Person"), related_name='Person')
	occurrence = models.ForeignKey('Occurrence', verbose_name=_(u"Occurrence"), related_name='Occurrence')
	date = models.DateField(verbose_name=_(u"Date"))
	time = models.TimeField(verbose_name=_(u"Time"))
	
	address = models.ForeignKey('Address', verbose_name=_(u"Address"), related_name='Address')
	observation = models.CharField( max_length=255,
									verbose_name=_("Observation"), 
									help_text=_("enter a description for the event. Example to be given: to destroy, render useless or deteriorate alien thing."),
									null=True, 
									blank=True)
	image = models.ImageField(	verbose_name=_(u"Image"),
								help_text=_(u"Enter image to report."),
								upload_to = 'documents/image/report/%Y/%m/%d',
								null=True, 
								blank=True)	
	
	creation = models.DateTimeField(verbose_name=_(u'Creation'), default=timezone.now)
	exists = models.BooleanField(verbose_name=_(u"Exists"), default=True)

	def set_person(self, person):
		self.person = person


	def set_address(self, address):
		self.address = address

	def set_occurrence(self, occurrence):
		self.occurrence = occurrence

	def get_person(self):
		return self.person

	def get_occurrence(self):
		return self.occurrence

	def get_date(self):
		return self.date

	def get_time(self):
		return self.time

	def get_address(self):
		return self.address

	def get_observation(self):
		return self.observation


	def __unicode__(self):
		return unicode(self.get_occurrence())

	def delete(self):
		self.exists = False
		self.save()
		
	def restore(self):
		self.exists = True
		self.save()
	
	class Meta:
		ordering = ['-occurrence']
		verbose_name = _(u"Report")
		verbose_name_plural = _(u"Reports")

