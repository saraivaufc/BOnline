from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password
from django.db.models import Q


from bo.models import Person, GeneralUser, Organizer
from bo.management.permissions import group_permissions


class LoginForm(forms.Form):
    email = forms.CharField(label=_('Email'), help_text=_("Please enter you email."),
        widget=forms.TextInput(), 
        error_messages={'required': _('Please enter you email.')} )
    password = forms.CharField(label=_('Password'), help_text=_('Please enter you password.'),
        widget=forms.PasswordInput(),
        error_messages={'required': _('Please enter you password.')})

    class Meta:
        fields = ("email", "password")

class RegisterForm(ModelForm):
    password2 = forms.CharField(label=_(u'Password confirmation'), widget=forms.PasswordInput)
    GROUPS = [
        ('generalUser',_('GeneralUser')),
        ('organizer',_('Organizer')),
    ]
    group = forms.ChoiceField(label=_("Group"), choices=GROUPS)
    key = forms.CharField(label=_("Key"), max_length=4, required=False,
        widget=forms.PasswordInput(), help_text=_("If you want to create a record in this group should have an access key for this, please contact the administrator."))
    class Meta:
        model= Person
        fields = ("first_name", "last_name","email","password", "password2", "group","key")

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError(_("Passwords don't match"))
        return password2

class GeneralUserRegisterForm(RegisterForm):
    class Meta(RegisterForm.Meta):
        model = GeneralUser

class OrganizerRegisterForm(RegisterForm):
    class Meta(RegisterForm.Meta):
        model = Organizer
    