from django.conf import settings
from django.db import models
from utils import constants
        
class Machine(models.Model):
    name = models.CharField(max_length=1)
    slots = models.JSONField(default=constants.default_slot_status)

    def __str__(self):
        return self.name

    def get_slot_status(self):
        slot_available = []
        for i, is_available in enumerate(self.slots):
            if is_available: slot_available.append(i)
        return slot_available
    
    def booked_slot(self, slot_pos):
        print(f'booked_slot : {slot_pos}')
        if self.slots[slot_pos]: 
            self.slots[slot_pos] = False
            self.save()
            return
        
        print(f'unbooked_slot : {slot_pos}')

        self.slots[slot_pos] = True
        self.save()
        return

class Booking(models.Model):
    neighbor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, null=True, blank=True)
    slot = models.IntegerField(null=True, blank=True)

    def get_machine_slots(self):
        return self.machine.slots
    
    def __str__(self):
        return f'neighbor : {self.neighbor.name}\nmachine : {self.machine.name}\nslot : {self.slot}'

    class Meta:
        unique_together = ('neighbor', 'machine', 'slot')