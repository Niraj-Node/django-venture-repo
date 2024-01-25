# forms.py
from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    mobile_number = forms.CharField(min_length=10,max_length=14)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    dob = forms.DateField(input_formats=['%d-%m-%y'])
    hobbies = forms.CharField(widget=forms.Textarea)