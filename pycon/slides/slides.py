from pycon.schedule.models import Room, Slot


def gen_prev_text(slot):
    text = ""

    if getattr(slot, 'kind_label', None) is None:
        return ''

    if slot.kind_label == 'talk' and slot.presenter:
        text = "Thanks for viewing {}'s talk!".format(slot.presenter)
    elif slot.kind_label == 'tutorial' and slot.presenter:
        text = "Thanks for attending {}'s tutorial!".format(slot.presenter)
    else:
        text = slot.content_override
    if slot.feedback_url:
        text += " Please give feedback at {}.".format(slot.feedback_url)
    return text


class Slides(object):

    def __iter__(self):
        for room in Room.objects.all():
            slots = Slot.objects.filter(slotroom__room=room).order_by('day__date', 'start')
            prev_slot = None

            for next_slot in slots:
                result = {
                    'prev_start': getattr(prev_slot, 'start', None),
                    'prev_end': getattr(prev_slot, 'end', None),
                    'prev_text': gen_prev_text(prev_slot),
                    'next_start': getattr(next_slot, 'start', None),
                    'next_end': getattr(next_slot, 'end', None),
                }
                yield result
                prev_slot = next_slot
