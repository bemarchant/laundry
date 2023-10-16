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
        return f'{self.id} - {self.name}'

class Apartment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField()    
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

class Neighbor(AbstractUser):
    print('Neighbor')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, blank=True, null=True)
    age = models.IntegerField(default=30)
    gender = models.CharField(max_length=1, default="O", choices=[('M', 'Hombre'), ('F', 'Mujer'), ('O', 'Otro')])
    phone = models.CharField(max_length=14, default='(+56)9XXXXXXXX')
    
    def __str__(self):
        return f'{self.id} - {self.apartment}'
    
    def delete(self, *args, **kwargs):
        print('delete')
        superneighbor = SuperNeighbor.objects.first()
        if not superneighbor:
            return super().delete(*args, **kwargs)
        if self == superneighbor.user:
            return
        else:
            return super().delete(*args, **kwargs)

class SuperNeighbor(models.Model):
    print('SuperNeighbor')
    user = models.OneToOneField(Neighbor, on_delete=models.CASCADE, related_name='superneighbor', null=True, blank=True)

    def __str__(self):
        return f'SuperNeighbor: {self.user}'
    
    def save(self, *args, **kwargs):     
        super_neighbor_group, created = Group.objects.get_or_create(name='allow_superneighbor')
        superneighbor = SuperNeighbor.objects.first()

        if not superneighbor:
            print(' if not superneighbor')
            self.user.groups.add(super_neighbor_group)
            superneighbor = SuperNeighbor()
            superneighbor.user = self.user
            superneighbor.user.is_staff = True
            superneighbor.user.is_superuser = True

            super().save(*args, **kwargs)
            return
        
        if self.user == superneighbor.user:
            print('self.user == superneighbor.user')

            return
        
        if self.user != superneighbor.user:
            print( "self.user != superneighbor.user")
            superneighbor.user.is_staff = False
            superneighbor.user.is_superuser = False
            superneighbor.user.groups.remove(super_neighbor_group)
            superneighbor.user = self.user
            superneighbor.user.groups.add(super_neighbor_group)
            superneighbor.user.is_staff = True
            superneighbor.user.is_superuser = True
            
            super().save(*args, **kwargs)
            return

# permission = Permission.objects.create(
#     codename='can_do_superneighbor',
#     name='Can do Super',
#     content_type=ContentType.objects.get_for_model(SuperNeighbor),
# )