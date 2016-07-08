from django.contrib import admin

# Register your models here.
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo','phone']

admin.site.register(Profile,ProfileAdmin)