from django import forms
from pycon.mailing.models import Mailing
from django.utils.translation import ugettext_lazy as _


class MailingSignUpForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': _('Name'),
        }),
    )

    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'placeholder': _('Email'),
        }),
    )

    class Meta:
        model = Mailing
        fields = ['name', 'email']
