from django import forms
from .models import Neighbor, Apartment

class NeighborSignupForm(forms.ModelForm):
    class Meta:
        model = Neighbor
        fields = ['name', 'age', 'gender', 'phone', 'email', 'apartment']
