from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone

class Address(models.Model):
    cep = models.CharField(max_length=9, verbose_name=_("CEP"), help_text="Format: XXXXX-XXX")
    street = models.CharField(max_length=255, verbose_name=_(u"Street"), help_text=_(u'Please enter street.'))
    district = models.CharField(max_length=255, verbose_name=_(u"District"), help_text=_(u'Please enter district.'))
    city = models.CharField(max_length=255, verbose_name=_(u"City"), help_text=_(u'Please enter city.'))
    state = models.CharField(max_length=255, verbose_name=_(u"State"), help_text=_(u'Please enter state.'))

    creation = models.DateTimeField(verbose_name=_(u'Creation'), default=timezone.now)
    exists = models.BooleanField(verbose_name=_(u"Exists"), default=True)

    def get_cep(self):
        return self.cep
    def get_street(self):
        return self.street
    def get_district(self):
        return self.district
    def get_city(self):
        return self.city
    def get_state(self):
        return self.state

    def __unicode__(self):
        return self.cep

    def delete(self):
        self.exists = False
        self.save()
        
    def restore(self):
        self.exists = True
        self.save()
    
    class Meta:
        ordering = ['cep']
        verbose_name = _(u"Address")
        verbose_name_plural = _(u"Addreses")