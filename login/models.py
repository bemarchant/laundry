from django.db import models

class Apartment(models.Model):
    apartment_id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.number

class Neighbor(models.Model):
    neighbor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Neighborhood(models.Model):
    neighbors = models.ManyToManyField(Neighbor)

    def __str__(self):
        return "Neighborhood"
