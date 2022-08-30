from django.contrib import admin
from .models import RegisterProvider, RegisterBuyer


@admin.register(RegisterProvider)
class AdminRegisterProvider(admin.ModelAdmin):
    list_display = ('id', 'email', 'city')
    list_filter = ('email', 'city', 'phone_number')
    search_fields = ('email', 'city', 'phone_number')


@admin.register(RegisterBuyer)
class AdminRegisterBuyer(admin.ModelAdmin):
    list_display = ('id', 'email', 'city')
    list_filter = ('email', 'city', 'phone_number')
    search_fields = ('email', 'city', 'phone_number')
