from django.contrib import admin
from .models import Ornament, PersonName, City, DailyBalanceSheet
# Register your models here.

class OrnamentAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_per_page = 25
    ordering = ['name']
admin.site.register(Ornament, OrnamentAdmin)

class PersonNameAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_per_page = 25
    ordering = ['name']
admin.site.register(PersonName, PersonNameAdmin)

class CityAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_per_page = 25
    ordering = ['name']
admin.site.register(City, CityAdmin)