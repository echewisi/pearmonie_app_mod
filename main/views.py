from django.shortcuts import render, redirect
from .models import PatronUser,CustomUser, CustomOrganization, InvoiceModel, Products 
from .forms import UserCreationForm, PatronOrganizationForm

def registration_view(request):
    if request.user.is_authenticated:
        redirect("dashboard")
    if request.method=="POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            
        
"""what i wish to achieve in this view is to  """
# Create your views here.
