from django.conf.urls import url

from pycon.mailing.views import MailingSignUpView

urlpatterns = [
    url(r'^signup/', MailingSignUpView.as_view(), name='mailing_list'),
]
