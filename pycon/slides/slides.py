# -*- coding: utf-8 -*-
from django.utils.text import slugify
from django.conf import settings
from pycon.schedule.models import Room, Slot, Day


def gen_prev_text(slot):
    if slot is None:
        return ''

    if slot.kind_label == 'talk' and slot.presenter:
        text = "Thanks for attending {}'s talk!".format(slot.presenter)
    elif slot.kind_label == 'tutorial' and slot.presenter:
        text = "Thanks for attending {}'s tutorial!".format(slot.presenter)
    else:
        text = slot.content_override
    return text


def get_next_text(slot):
    if slot is None:
        return ''

    if slot.content_override:
        return slot.content_override

    presenter = getattr(slot, 'presenter', '')
    title = getattr(slot, 'title', '')
    if presenter:
        if title:
            return '<i>&ldquo;{}&rdquo;</i> <br/> by {}'.format(title, presenter)
        return '{} by {}'.format(slot.kind_label, presenter)
    return title


def get_slug(slot):
    if slot.kind_label in ['tutorial', 'talk'] and slot.presenter:
        return slugify(slot.presenter)
    return slugify(slot.content_override)


class Slides(object):

    def __iter__(self):
        for room in Room.objects.all():
            for day in Day.objects.all():
                slots = Slot.objects.filter(slotroom__room=room, day=day).order_by('start')
                prev_slot = None

                for next_slot in slots:
                    result = {
                        'room': room,
                        'day': day,
                        'prev_start': getattr(prev_slot, 'start', None),
                        'prev_end': getattr(prev_slot, 'end', None),
                        'prev_text': gen_prev_text(prev_slot),
                        'feedback_url': getattr(prev_slot, 'feedback_url', None),
                        'next_start': getattr(next_slot, 'start', None),
                        'next_end': getattr(next_slot, 'end', None),
                        'next_text': get_next_text(next_slot),
                        'slug': get_slug(next_slot),
                        'BASE_DIR': settings.BASE_DIR
                    }
                    yield result
                    prev_slot = next_slot
