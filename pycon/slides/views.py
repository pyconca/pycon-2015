from django.http.response import HttpResponse
from django.template import loader
from pycon.schedule.models import Day
from pycon.schedule.timetable import TimeTable


def slides(request):
    for day in Day.objects.all():
        timetable = TimeTable(day)
        prev_row = None
        for next_row in timetable:
            context = {
                'prev_row': prev_row,
                'next_row': next_row
            }
            print(loader.render_to_string('slides/slide.html', context))
            prev_row = next_row
    return HttpResponse()
