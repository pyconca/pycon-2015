import errno
import os
import shutil
from uuid import uuid4
from django.http.response import HttpResponse
from django.template import loader
from pycon.slides.slides import Slides


def slides(request):
    base_dir = '/tmp/slides.' + uuid4().hex
    html_dir = os.path.join(base_dir, 'html')
    os.makedirs(html_dir)
    for slide in Slides():
        room_dir = os.path.join(html_dir, slide['room'].name)
        try:
            os.makedirs(room_dir)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
        slide_path = os.path.join(room_dir, slide['next_start'].strftime('%H%M%S')) + '.html'
        html = loader.render_to_string('slides/slide.html', slide)
        slide_file = open(slide_path, 'w')
        slide_file.write(html)
        slide_file.close()
    shutil.rmtree(base_dir)
    return HttpResponse()
