from django.contrib import admin
from .models import MyUser

from django.contrib.auth.admin import UserAdmin



class MyUserAdminConf(UserAdmin):

    ordering           = ('-date_joined',)
    list_display       = (
        'email',
        'first_name',
        'last_name',
        'last_login',
        'is_superuser',
        'is_active'
    )

    list_display_links = (
        'email',
        'first_name',
        'last_name',
    )


     
    readonly_fields = ["date_joined","last_login"]
    
    filter_horizontal=()
    list_filter=()
    fieldsets=()
    



# Register your models here.



admin.site.register(MyUser,MyUserAdminConf)