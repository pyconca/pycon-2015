from django.http.response import HttpResponse
from django.template import loader
from pycon.slides.slides import Slides


def slides(request):
    for slide in Slides():
        print(loader.render_to_string('slides/slide.html', slide))
    return HttpResponse()
