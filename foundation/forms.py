from django import forms
from .models import Donation, Volunteer
class DonationForm(forms.ModelForm):
    class Meta:
        model=Donation
        fields=['name','email','address','amount','custom_amount','cause']
    def clean(self):
        c=super().clean(); amount=c.get('amount'); custom=c.get('custom_amount')
        if amount=='custom' and not custom: raise forms.ValidationError('Please enter custom amount')
        return c
class VolunteerForm(forms.ModelForm):
    class Meta:
        model=Volunteer
        fields=['full_name','email','phone','interest','availability']
    def clean_phone(self):
        p=self.cleaned_data['phone']
        if not p.isdigit() or len(p)!=10: raise forms.ValidationError('Enter valid 10 digit phone number')
        return p
