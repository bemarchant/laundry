from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import Group, User
from django.core.exceptions import ValidationError

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
        if self.phone:
            return self.phone
        else: 
            return 'no phone'

class SuperNeighbor(models.Model):

    user = models.OneToOneField(Neighbor, on_delete=models.CASCADE, related_name='superneighbor', null=True, blank=True)

    def save(self, *args, **kwargs):     
        super_neighbor_group, created = Group.objects.get_or_create(name='allow_superneighbor')
        superneighbor = SuperNeighbor.objects.first()
        
        if not superneighbor.user:
            self.user.groups.add(super_neighbor_group)
            superneighbor.user = self.user
            super().save(*args, **kwargs)
            return
        
        if self.user == superneighbor.user:
            return
        
        if self.user != superneighbor.user:
            superneighbor.user.groups.remove(super_neighbor_group)
            self.user.groups.add(super_neighbor_group)
            superneighbor.user = self.user
            super().save(*args, **kwargs)
            return

    def __str__(self):
        return f'SuperNeighbor: {self.user}'

