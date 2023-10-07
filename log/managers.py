from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _







class MyUserManger(BaseUserManager): 

    """
     
     custom user manager to manage our user function to create user and admin 

     

    """
    def create_user(self,email,first_name,last_name,password,**other_fields):

        if not email:
            raise ValueError(_("You Must provide and Email Address"))
     
        email = self.normalize_email(email)
        user  = self.model(email=email,first_name=first_name,last_name=last_name,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,first_name,last_name,password,**other_fields):
        
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'super user must assigned to is_staff=True')
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser Must be assigned to is_superuser=True')
        
        return self.create_user(email,first_name,last_name,password,**other_fields)
    
