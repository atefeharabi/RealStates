from django.contrib import admin
from .models import User, Address, House, Apartment, Shop


# Register your models here.
admin.site.register(User)
admin.site.register(Address)
admin.site.register(House)
admin.site.register(Apartment)
admin.site.register(Shop)
