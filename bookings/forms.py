from django import forms # type: ignore
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'date', 'time', 'guests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.DateInput(attrs={'type': 'time'}),
        }
    # Validation for 'guests' field
    def clean_guests(self):
        guests = self.cleaned_data.get('guests')
        if guests < 1:
            raise forms.ValidationError("Guests must be at least 1.")
        return guests