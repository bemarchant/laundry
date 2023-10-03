from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.contenttypes.models import ContentType
import uuid

class Neighborhood(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default="")

    def __str__(self):
        return "Neighborhood"

class Apartment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField()    
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

class Neighbor(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, blank=True, null=True)
    age = models.IntegerField(default=30)
    gender = models.CharField(max_length=1, default="O", choices=[('M', 'Hombre'), ('F', 'Mujer'), ('O', 'Otro')])
    phone = models.CharField(max_length=14, default='(+56)9XXXXXXXX')

    def __str__(self):
        return self.id

class SuperNeighbor(Neighbor):
    class Meta:
        proxy = True

