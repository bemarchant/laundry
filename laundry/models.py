from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models
from django.db.models import Q
from home.models import Neighbor
import datetime
import uuid
from django.utils import timezone

class Machine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'id: {self.id}\nname : {self.name}'


class Booking(models.Model):
    DURATION_CHOICES = (
        (15, '15 minutos'),
        (30, '30 minutos'),
        (45, '45 minutos'),
        (60, '60 minutos'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    neighbor = models.ForeignKey(Neighbor, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, null=True, blank=True)
    duration = models.PositiveIntegerField(default=15, choices=DURATION_CHOICES)
    start_time = models.TimeField(default=datetime.date.today())

    def __str__(self):
        return f'booking : {self.id}'
    
    def end_time(self):
        return self.start_time + timezone.timedelta(minutes=self.duration)
    
    def clean(self):
        if self.duration % 15 != 0:
            raise ValidationError('Duration time must be a multiple of 15 minutes')
        
        if self.start_time.minute % 15 != 0:
            raise ValidationError('Start time must be a multiple of 15 minutes')
    
    def save(self, *args, **kwargs): 
        super().save(*args, **kwargs)