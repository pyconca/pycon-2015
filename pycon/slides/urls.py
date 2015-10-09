from django.conf.urls import url
from pycon.slides.views import slides

urlpatterns = [
    url(r"^$", slides, name='slides'),
]
