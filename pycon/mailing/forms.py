from django import forms
from pycon.mailing.models import Mailing


class MailingSignUpForm(forms.ModelForm):

    class Meta:
        model = Mailing
        fields = ['name', 'email']
