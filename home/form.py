from django.forms import ModelForm
from .models import Contact, Donation


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'       