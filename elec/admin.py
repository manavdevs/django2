from django.contrib import admin
from .models import Elec
# Register your models here.

@admin.register(Elec)
class ElecAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','quants')    