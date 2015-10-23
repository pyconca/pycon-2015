import os
import shutil
import subprocess
from uuid import uuid4
from django.conf import settings
from django.http.response import HttpResponse
from django.template import loader
from pycon.schedule.models import Room
from pycon.slides.slides import Slides


def slides(request):
    base_dir = '/tmp/slides.' + uuid4().hex
    html_dir = os.path.join(base_dir, 'html')
    png_dir = os.path.join(base_dir, 'png')
    try:
        os.makedirs(html_dir)
        html_paths = []
        for room in Room.objects.all():
            os.makedirs(os.path.join(html_dir, room.name))
            os.makedirs(os.path.join(png_dir, room.name))

        for slide in Slides():
            html_room_dir = os.path.join(html_dir, slide['room'].name)
            html_path = os.path.join(html_room_dir, slide['next_start'].strftime('%H%M%S')) + '.html'
            html = loader.render_to_string('slides/slide.html', slide)
            html_file = open(html_path, 'w')
            html_file.write(html)
            html_file.close()
            html_paths.append(html_path)

        for html_path in html_paths:
            png_path = html_path.replace('/html/', '/png/')\
                                .replace('.html', '.png')
            png_dir, png_name = os.path.split(png_path)
            subprocess.check_call([
                settings.WEBKIT2PNG_PATH,
                '-F',  # just full size image
                '-W',
                str(settings.SLIDE_WIDTH),
                '-H',
                str(settings.SLIDE_HEIGHT),
                '-D',
                png_dir,
                '-o',
                png_name,
                html_path,
            ])

    finally:
        shutil.rmtree(base_dir)
    return HttpResponse()
