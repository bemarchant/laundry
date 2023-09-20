from django import forms


class BookingForm(forms.Form):
    date = forms.CharField()
    machine = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
