from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['duration', 'start_time']

    duration = forms.IntegerField(
        label='Booking Duration (minutes)',
        min_value=15,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter booking duration in minutes'})
    )

    start_time = forms.DateTimeField(
        label='Booking Start Time (hour:minute)',
        widget=forms.TextInput(attrs={'placeholder': 'Enter booking start time in hour:minute format'}),
        input_formats=['%H:%M'],
        required=True
    )

    def clean_start_time(self):
        start_time = self.cleaned_data.get('start_time')

        # Check if the specified start time is in the past
        if start_time <= timezone.now():
            raise ValidationError('Start time must be in the future.')

        return start_time
