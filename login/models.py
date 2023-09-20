from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import string

class Apartment(models.Model):
    apartment_id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.number
    
class Neighbor(AbstractUser):
    neighbor_id = models.CharField(max_length=8, unique=True, primary_key=True)
    name = models.CharField(max_length=100, default='Benja Marchant')
    age = models.IntegerField(default=30)
    gender = models.CharField(max_length=1, default="O", choices=[('M', 'Hombre'), ('F', 'Mujer'), ('O', 'Otro')])
    apartment = models.CharField(max_length=100, default='802')
    phone = models.CharField(max_length=14, default='(+56)9XXXXXXXX')

    def generate_neighbor_id(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def save(self, *args, **kwargs):
        if not self.neighbor_id:
            self.neighbor_id = self.generate_neighbor_id()

        super().save(*args, **kwargs)

class Neighborhood(models.Model):
    neighbors = models.ManyToManyField(Neighbor)
    
    def __str__(self):
        return "Neighborhood"
