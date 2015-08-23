from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _

from pycon.core.views import PyconTemplateView
from pycon.mailing.forms import MailingSignUpForm


class MailingSignUpView(PyconTemplateView):
    def post(self, request, return_url='home'):
        form = MailingSignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Thanks for signing up!'))
            return redirect(return_url)
        return self.render_to_response({
            'mailing_form': form,
        })
