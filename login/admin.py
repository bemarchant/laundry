from django.contrib import admin
from .models import Apartment, Neighbor, Neighborhood,SuperNeighbor

class NeighborAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name','last_name', 'email', 'apartment', 'age', 'gender', 'phone')

admin.site.register(Apartment)
admin.site.register(Neighborhood)
admin.site.register(Neighbor, NeighborAdmin)
admin.site.register(SuperNeighbor)

