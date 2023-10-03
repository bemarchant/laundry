from django.conf import settings
from django.db import models 
from login.models import Neighbor
from utils import constants
import uuid


class Machine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'id: {self.id}\nname : {self.name}\nslots : {self.slots}'

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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    neighbor = models.ForeignKey(Neighbor, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, null=True, blank=True)
    slot = models.IntegerField(null=True, blank=True)

    def get_machine_slots(self):
        return self.machine.slots
    
    def __str__(self):
        return f'neighbor : {self.neighbor.name}\nmachine : {self.machine.name}\nslot : {self.slot}'

    class Meta:
        unique_together = ('neighbor', 'machine', 'slot')


