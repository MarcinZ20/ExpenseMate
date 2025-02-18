from django.contrib import admin
from .models import User, UserAddress, UserDetails

admin.site.register(User)
admin.site.register(UserDetails)
admin.site.register(UserAddress)
