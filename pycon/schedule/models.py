from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="speaker_photos", blank=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Day(models.Model):
    date = models.DateField(unique=True)
    
    def __str__(self):
        return "%s" % self.date
    
    class Meta:
        ordering = ["date"]

class Room(models.Model):
    name = models.CharField(max_length=100)
    
    order = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["order"]

class SlotKind(models.Model):
    label = models.CharField(max_length=50)
    
    def __str__(self):
        return self.label

class Slot(models.Model):
    day = models.ForeignKey(Day)
    kind = models.ForeignKey(SlotKind)
    start = models.TimeField()
    end = models.TimeField()
    content_override = models.TextField(blank=True)
    
    def assign(self, content):
        """
        Assign the given content to this slot and if a previous slot content
        was given we need to unlink it to avoid integrity errors.
        """
        self.unassign()
        content.slot = self
        content.save()
    
    def unassign(self):
        """
        Unassign the associated content with this slot.
        """
        content = self.content
        if content and content.slot_id:
            content.slot = None
            content.save()
    
    @property
    def content(self):
        """
        Return the content this slot represents.
        @@@ hard-coded for presentation for now
        """
        try:
            return self.content_ptr
        except ObjectDoesNotExist:
            return None
    
    @property
    def start_datetime(self):
        return datetime.datetime(
            self.day.date.year,
            self.day.date.month,
            self.day.date.day,
            self.start.hour,
            self.start.minute)
    
    @property
    def end_datetime(self):
        return datetime.datetime(
            self.day.date.year,
            self.day.date.month,
            self.day.date.day,
            self.end.hour,
            self.end.minute)
    
    @property
    def length_in_minutes(self):
        return int(
            (self.end_datetime - self.start_datetime).total_seconds() / 60)
    
    @property
    def rooms(self):
        return Room.objects.filter(pk__in=self.slotroom_set.values("room"))
    
    def __str__(self):
        roomlist = ' '.join(map(lambda r: r.__str__(), self.rooms))
        return "%s %s (%s - %s) %s" % (self.day, self.kind, self.start, self.end, roomlist)
    
    class Meta:
        ordering = ["day", "start", "end"]

class SlotRoom(models.Model):
    slot = models.ForeignKey(Slot)
    room = models.ForeignKey(Room)
    
    def __str__(self):
        return "%s %s" % (self.room, self.slot)
    
    class Meta:
        unique_together = [("slot", "room")]
        ordering = ["slot", "room__order"]

class Presentation(models.Model):
    slot = models.OneToOneField(Slot, null=True, blank=True, related_name="content_ptr")
    title = models.CharField(max_length=100)
    description = models.TextField()
    speaker = models.ForeignKey(Speaker, related_name="presentations")
    additional_speakers = models.ManyToManyField(Speaker, related_name="copresentations", blank=True)
    cancelled = models.BooleanField(default=False)
    
    def speakers(self):
        yield self.speaker
        for speaker in self.additional_speakers.all():
            if speaker.user:
                yield speaker
    
    def __str__(self):
        return "%s (%s)" % (self.title, self.speaker)

    class Meta:
        ordering = ["slot"]

class Session(models.Model):
    day = models.ForeignKey(Day, related_name="sessions")
    slots = models.ManyToManyField(Slot, related_name="sessions")

    def sorted_slots(self):
        return self.slots.order_by("start")

    def start(self):
        slots = self.sorted_slots()
        if slots:
            return list(slots)[0].start
        else:
            return None

    def end(self):
        slots = self.sorted_slots()
        if slots:
            return list(slots)[-1].end
        else:
            return None

    def __str__(self):
        start = self.start()
        end = self.end()
        if start and end:
            return "%s: %s - %s" % (
                self.day.date.strftime("%a"),
                start.strftime("%X"),
                end.strftime("%X")
            )
        return ""