from django.forms import ModelForm, TextInput, EmailInput
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import check_password

from bo.models import Person, General, Organizer, Address
from bo.management.permissions import group_permissions
from bo.widgets import AdvancedFileInput


class LoginForm(forms.Form):
    email = forms.CharField(label=_('Email'), help_text=_("Please enter you email."),
        widget=forms.EmailInput(), 
        error_messages={'required': _('Please enter you email.')} )
    password = forms.CharField(label=_('Password'), help_text=_('Please enter you password.'),
        widget=forms.PasswordInput(),
        error_messages={'required': _('Please enter you password.')})

    class Meta:
        fields = ("email", "password")

class RegisterForm(ModelForm):
    password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_(u'Password confirmation'), widget=forms.PasswordInput)
    GROUPS = [
        ('general',_('General')),
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

class ProfileForm(ModelForm):
    class Meta:
        model= Person
        fields = ("first_name","last_name","email","profile_image")
        widgets = {
            'first_name': TextInput(attrs={'required': 'required', 'autofocus': 'True'}),
            'last_name': TextInput(attrs={'required': 'required'}),
            'email': EmailInput(attrs={'required': 'required'}),
            'profile_image': AdvancedFileInput(attrs={}),
        }
    def clean_profile_image(self):
        profile_image = self.cleaned_data["profile_image"]
        try:
            if profile_image and profile_image.name.find('askmath') == -1:
                hash = hashlib.md5(profile_image.read()).hexdigest()
                profile_image.name = "bo_" + "".join((hash, ".", profile_image.name.split(".")[-1]))
        except:
            pass
        return profile_image

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = ("cep", "street", "district", "city", "state")

class GeneralRegisterForm(RegisterForm):
    class Meta(RegisterForm.Meta):
        model = General

class OrganizerRegisterForm(RegisterForm):
    class Meta(RegisterForm.Meta):
        model = Organizer