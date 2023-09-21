from django.conf import settings
from django.db import models
from datetime import date
from utils import constants
        
class Machine(models.Model):
    name = models.CharField(max_length=1)
    slots = constants.SLOT_AVAILABLE

    def __str__(self):
        return self.name

    def get_slot_status(self):
        slot_available = []
        for i, is_available in enumerate(self.slots):
            if is_available: slot_available.append(i)
        return slot_available
    
    def booked_slot(self, slot_pos):
        if self.slots[slot_pos]: 
            self.slots[slot_pos] = False
            return
        self.slots[slot_pos] = True
        return

class Booking(models.Model):
    today = date.today()
    
    neighbor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.neighbor.neighbor} - {self.machine}"


