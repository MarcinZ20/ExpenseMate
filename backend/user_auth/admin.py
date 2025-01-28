from django.contrib import admin
from .models import CustomUser, CustomUserAddress, CustomUserDetails

admin.site.register(CustomUser)
admin.site.register(CustomUserDetails)
admin.site.register(CustomUserAddress)
