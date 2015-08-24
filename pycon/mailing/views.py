from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _

from pycon.core.views import PyconTemplateView
from pycon.mailing.forms import MailingSignUpForm


class MailingSignUpView(PyconTemplateView):

    template_name = 'home.html'

    def post(self, request):
        form = MailingSignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Thanks for signing up!'))
            return redirect(request.META.get('HTTP_REFERER'))
        return self.render_to_response({'mailing_form': form,})
