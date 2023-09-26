from django import forms


class BookingForm(forms.Form):
    neighbor = forms.CharField()
    machine = forms.CharField()

    def __init__(self, *args, **kwargs):
        print('__init__')
        super().__init__(*args, **kwargs)