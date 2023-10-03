from .models import Neighbor
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation

class NeighborSignupForm(UserCreationForm):
    class Meta:
        model = Neighbor
        fields = ['age', 'username','first_name','last_name','gender', 'apartment', 'phone', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            try:
                password_validation.validate_password(password1, self.instance)
            except forms.ValidationError as error:
                self.add_error('password1', error)
        return password1
    

class NeighborLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username-input'}))
    password = forms.CharField(widget=forms.PasswordInput)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
