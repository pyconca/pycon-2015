from pycon.schedule.models import Day, Room, Slot


class Slides(object):

    def __iter__(self):
        for room in Room.objects.all():
            slots = Slot.objects.filter(slotroom__room=room).order_by('day__date', 'start')
            prev_slot = None

            for next_slot in slots:
                result = {
                    'prev_start': getattr(prev_slot, 'start', None),
                    'prev_end': getattr(prev_slot, 'end', None),
                    'next_start': getattr(next_slot, 'start', None),
                    'next_end': getattr(next_slot, 'end', None),
                }
                yield result
                prev_slot = next_slot
