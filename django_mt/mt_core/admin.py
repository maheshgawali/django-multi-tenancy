
from django.contrib import admin
from .models import DbDetails, DomainDb

@admin.register(DomainDb)
class DbDetailsAdmin(admin.ModelAdmin):
    pass

@admin.register(DbDetails)
class DbDetailsAdmin(admin.ModelAdmin):
    pass
