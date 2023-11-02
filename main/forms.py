from django import forms
from .models import PatronUser, CustomOrganization, CustomUser
from django.contrib.auth.forms import UserCreationForm

class PatronUserRegsitrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'name', 'account_number', 'contact')
class PatronOrganizationForm(forms.Form):
    class Meta:
        model = CustomOrganization
        fields = ('username', 'password1', 'password2', 'name', 'company_contact')
