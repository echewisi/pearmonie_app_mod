from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField





PARTRON=(("organisations", "Organisations"),
        ("users", "Users"))

class PatronUser(AbstractUser):
    """remember to make this a uuid field"""
    name= models.CharField(max_length= 200, blank= False, default="anonymous")
    patron_choice= models.CharField(choices=PARTRON)
    
    # def add_to_user_model(self):
    #         CustomUser.objects.update_or_create(self)
    #         self.save()
    
    # def add_to_org_model(self):
    #     if self.patron_choice== "organisations".lower():
    #         CustomOrganization.objects.update_or_create(self)
    #         self.save()
            
class CustomUser(PatronUser):
    account_number= models.IntegerField(max_length= 255)
    contact= PhoneNumberField(blank= True)
    services= models.ManyToManyField("Products", blank= True )
    #this field below tracks the total number of transaction the user deals with, be it a debit or a credit
    total_transaction= models.PositiveIntegerField(default=0)
    funds= models.DecimalField(default=0, max_digits=10, decimal_places=2)
    
    def increment_total_transaction(self):
        self.total_transaction += 1
        self.save()

class CustomOrganization(PatronUser):
    services= models.ManyToManyField("Products", blank= True )
    company_contact= PhoneNumberField(blank= False)
    #this field below tracks the total number of transaction the user deals with, be it a debit or a credit
    total_transaction= models.PositiveIntegerField(default=0)
    funds= models.DecimalField(default=0, max_digits=10, decimal_places=2)

#this invoice model belongs to user/organization. it could be extended to add more features as needed by the app
class InvoiceModel(models.Model):
    manager= models.OneToOneField(PatronUser, on_delete= models.CASCADE)
    due_date= models.DateTimeField()
    working_hours= models.IntegerField(max_length=10, blank=False)
    
    
class Products(models.Model):
    name= models.CharField(max_length= 255, blank= False)
    description= models.CharField(max_length= 255, blank= True)
    price= models.DecimalField(default=0, max_digits=10, decimal_places=2)
    quantity= models.PositiveIntegerField(max_length=400, blank= True, default=1)
    finished= models.BooleanField(default= False)

class Customers(models.Model):
    trader= models.ForeignKey(PatronUser, on_delete= models.CASCADE, primary_key= True)
    customer_name= models.CharField(max_length= 255, blank= False, default= 'customer')
    contact= PhoneNumberField()
    email_address= models.EmailField()
    paid= models.BooleanField(default= False)
    
    
    
    
    
    

# Create your models here.
