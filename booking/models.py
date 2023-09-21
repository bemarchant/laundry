from django.conf import settings
from django.db import models
from datetime import date

class Machine(models.Model):
    name = models.CharField(max_length=1)

    def __str__(self):
        return self.name

    def get_available_slots(self, date):
        pass

class Booking(models.Model):
    today = date.today()
    neighbor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, default="1")
    date = models.DateField()
    slot = models.CharField(max_length=10, default="1")

    def __str__(self):
        return f"{self.neighbor.username} - {self.date}"


