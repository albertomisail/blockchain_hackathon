from django import forms
from .models import Hospital, Doctor
from datetime import date

class LoginForm(forms.Form):
    client_id = forms.IntegerField()
    password = forms.CharField(max_length=100)

class CheckupForm(forms.Form):
    hospital = forms.ChoiceField(choices=[(entry.name, entry.name) for entry in Hospital.objects.all()])
    doctor = forms.ChoiceField(choices=[(entry.person.name, entry.person.name) for entry in Doctor.objects.all()])
    date = forms.DateField(initial=date.today)
