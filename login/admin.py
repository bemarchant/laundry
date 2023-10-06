from django.contrib import admin
from .models import Apartment, Neighbor, Neighborhood,SuperNeighbor
from django.utils.html import format_html

class NeighborAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'display_groups', 'first_name', 'last_name', 'email', 'apartment', 'age', 'gender', 'phone')

    def display_groups(self, obj):
        groups = ", ".join([group.name for group in obj.groups.all()])
        return format_html(groups)

    display_groups.short_description = 'Groups'

class SuperNeighborAdmin(admin.ModelAdmin):
    model = SuperNeighbor

admin.site.register(Apartment)
admin.site.register(Neighborhood)
admin.site.register(Neighbor, NeighborAdmin)
admin.site.register(SuperNeighbor,SuperNeighborAdmin)

