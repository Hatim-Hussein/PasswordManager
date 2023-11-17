from django.contrib import admin
from .models import Password

# Register your models here.

@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'password', 'email', 'logo']
    search_fields = ['user__username', 'name', 'email']
