from django import forms
from .models import BookingDetails

class BookingForm(forms.ModelForm):
	class Meta:
		model = BookingDetails
		fields = '__all__'