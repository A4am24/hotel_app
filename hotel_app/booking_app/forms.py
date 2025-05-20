from django import forms
from .models import Hotel

class DisplayHotels(forms.ModelForm):
    class Meta:
        model=Hotel
        fields=['hotel_id', 'hotel_name', 'hotel_location', 'hotel_rating', 'price_per_night']

#class LoginForm(forms.ModelForm):
    #class