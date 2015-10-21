from django.contrib import admin
from pycon.schedule.models import *


class SlotRoomInline(admin.TabularInline):
    model = SlotRoom
    extra = 1


class SlotAdmin(admin.ModelAdmin):
    list_filter = ("day", "kind")
    list_display = ("day", "start", "end", "kind")
    inlines = [SlotRoomInline]


class RoomAdmin(admin.ModelAdmin):
    list_display = ["name", "order"]
    inlines = [SlotRoomInline]


class PresentationAdmin(admin.ModelAdmin):
    model = Presentation
    list_filter = ("cancelled", "slot")
    fields = (
        'slot',
        ('title', 'proposal_id',),
        'description',
        ('speaker', 'additional_speakers',),
        'cancelled',
        'feedback_url',
    )


admin.site.register(Day)
admin.site.register(
    SlotKind,
    list_display=["label"],
)
admin.site.register(
    SlotRoom,
    list_display=["slot", "room"]
)
admin.site.register(Room, RoomAdmin)
admin.site.register(Slot, SlotAdmin)
admin.site.register(Session)
admin.site.register(Presentation, PresentationAdmin)
admin.site.register(Speaker)
