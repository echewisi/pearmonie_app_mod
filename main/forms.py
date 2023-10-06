from django import forms
from .models import PatronUser, CustomOrganization, CustomUser


class PatronRegsitrationForm(forms.Form):
    name= forms.CharField()
    email
    password1

