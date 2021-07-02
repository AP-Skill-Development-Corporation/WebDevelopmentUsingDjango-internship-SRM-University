from .models import ContactUs
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"