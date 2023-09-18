from django.db import models
import random
import string

class Apartment(models.Model):
    apartment_id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.number

class Neighbor(models.Model):
    neighbor_id = models.CharField(max_length=8, unique=True, blank=True, null=True)

    def generate_neighbor_id(self):
        while True:
            neighbor_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            if not Neighbor.objects.filter(neighbor_id=neighbor_id).exists():
                self.neighbor_id = neighbor_id
                self.save()
                break

class Neighborhood(models.Model):
    neighbors = models.ManyToManyField(Neighbor)

    def __str__(self):
        return "Neighborhood"
