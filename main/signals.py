from .models import PatronUser, CustomOrganization, CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender= PatronUser )
def user_added(sender, instance, created, **kwargs ):
    if created:
        if instance.patron_choice == "users".lower():
            CustomUser.objects.update_or_create(instance)
        elif instance.patron_choice== "organizations".lower():
            CustomOrganization.objects.update_or_create(instance)