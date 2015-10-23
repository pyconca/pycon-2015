import os
import shutil
import subprocess
import zipfile
from uuid import uuid4
from django.conf import settings
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from pycon.schedule.models import Room
from pycon.slides.slides import Slides


def slides(request):
    def generate_html(slide):
        html_room_dir = os.path.join(html_dir, slide['room'].name)
        html_path = os.path.join(html_room_dir, slide['next_start'].strftime('%H%M%S')) + '.html'
        html = loader.render_to_string('slides/slide.html', slide)
        html_file = open(html_path, 'w')
        html_file.write(html)
        html_file.close()
        html_paths.append(html_path)

    def html_to_png(html_path):
        png_path = html_path.replace('/html/', '/png/')\
                            .replace('.html', '')
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
        return png_path + '-full.png'

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
            generate_html(slide)

        png_paths = []
        for html_path in html_paths:
            png_paths.append(html_to_png(html_path))

        zip_path = os.path.join(settings.MEDIA_ROOT, 'slides.zip')
        zip = zipfile.ZipFile(zip_path, 'w')
        for path in png_paths:
            dir, filename = os.path.split(path)
            zip.write(path, os.path.join(os.path.basename(dir), filename))
        response = HttpResponse(zip_path, content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="slides.zip"'
    finally:
        shutil.rmtree(base_dir)

    return redirect(settings.MEDIA_URL + '/slides.zip')
