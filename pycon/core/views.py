from django.views.generic.base import TemplateView

from pycon.mailing.forms import MailingSignUpForm


class PyconTemplateView(TemplateView):
    def render_to_response(self, context, **response_kwargs):
        if context.get('mailing_form') is None:
            context['mailing_form'] = MailingSignUpForm()
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )
